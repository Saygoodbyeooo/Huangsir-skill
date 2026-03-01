---
name: "markdown-translator"
description: "使用火山引擎API将英文Markdown学术论文翻译成中文双语对照格式。当用户需要翻译英文Markdown论文时调用。"
---

# Markdown 学术论文翻译工具

使用火山引擎（Volcano Engine）API 将英文 Markdown 格式的学术论文翻译成中文，生成中英双语对照文档。

## 功能特点

- **双语对照输出**：英文原文 + 中文翻译（引用块格式）
- **LaTeX公式保留**：保持所有数学公式不变
- **Markdown格式保留**：保持标题、加粗、列表等格式
- **图片路径保留**：图片路径不变，仅翻译说明文字
- **断点续传**：支持中断后继续翻译
- **错误重试**：指数退避重试机制

## 环境要求

1. **火山引擎API Key**：从 https://console.volcengine.com/ark/ 获取
2. **模型**：doubao-seed-1-8-251228（Doubao-Seed-1.8）
3. **Python依赖**：
   ```bash
   pip install openai
   ```

## 快速开始

### 1. 配置API密钥

在 `translator.py` 第6行填入你的API密钥：
```python
api_key = "你的API密钥"
```

### 2. 配置输入输出文件

在 `translator.py` 第152-153行修改文件路径：
```python
input_file = r"path/to/your/paper.md"
output_file = r"path/to/your/paper_bilingual.md"
```

### 3. 运行翻译

```bash
python translator.py
```

## 翻译脚本代码

```python
import os
import time
from openai import OpenAI

# 配置火山引擎 API
api_key = "你的API密钥"

client = OpenAI(
    base_url="https://ark.cn-beijing.volces.com/api/v3",
    api_key=api_key,
    timeout=60.0,
)

def translate_text(text, max_retries=5):
    """调用API翻译文本"""
    if not text or len(text.strip()) == 0:
        return text
    
    text = text.strip()
    if len(text) < 5:
        return text
    
    system_msg = """你是一个顶级的 AI 领域学术翻译专家。请将用户提供的英文 Markdown 段落翻译成中文。
【绝对规则】：
1. 保持所有的 Markdown 格式标记不变。
2. 绝对不要修改、翻译或破坏任何 LaTeX 数学公式（被 $ 或 $$ 包裹的内容）。
3. 专有名词保留英文。
4. 只输出翻译后的中文内容。"""
    
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model="doubao-seed-1-8-251228",
                max_completion_tokens=65535,
                reasoning_effort="minimal",
                messages=[
                    {"role": "system", "content": system_msg},
                    {"role": "user", "content": [{"type": "text", "text": text}]}
                ]
            )
            result = response.choices[0].message.content.strip()
            time.sleep(0.5)
            if result:
                return result
        except Exception as e:
            wait_time = 2 ** attempt
            print(f"\n      ⚠️ 网络/API报错: {str(e)[:40]}... 将在 {wait_time} 秒后重试", end="", flush=True)
            time.sleep(wait_time)
            
    return "[API连续报错，该段落翻译失败，请检查网络或API限额]"

def process_paragraph(para):
    """处理段落，生成双语对照"""
    para = para.strip()
    if not para:
        return para

    # 将 LaTeX 原生括号替换为 Markdown 美元符号
    para = para.replace(r'\(', '$').replace(r'\)', '$')
    para = para.replace(r'\[', '$$').replace(r'\]', '$$')

    # 跳过纯代码块、独立公式块、分隔符和纯图片路径
    if para.startswith('```') or para.startswith('$$') or para == '---' or para.startswith('!['):
        return para
    
    translated = translate_text(para)
    
    if translated and translated != para and not translated.startswith("[API连续报错"):
        translated_quoted = "> " + translated.replace('\n', '\n> ')
        return f"{para}\n\n{translated_quoted}"
    elif translated.startswith("[API连续报错"):
         return f"{para}\n\n> **{translated}**"
         
    return para

def translate_markdown_robust(file_path, output_path):
    """主函数：翻译Markdown文档"""
    print(f"🚀 启动增强版双语对照翻译 (支持断点续传)")
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    paragraphs = content.split('\n\n')
    total_paras = len(paragraphs)
    print(f"📚 原文档共 {total_paras} 个独立段落")
    
    # 断点续传逻辑
    start_index = 0
    existing_blocks = 0
    if os.path.exists(output_path):
        with open(output_path, "r", encoding="utf-8") as f:
            existing_text = f.read()
        for i, para in enumerate(paragraphs):
            fingerprint = para.strip()[:30]
            if fingerprint and fingerprint in existing_text:
                existing_blocks += 1
            elif not fingerprint:
                existing_blocks += 1
            else:
                break
        
        start_index = existing_blocks
        if start_index > 0 and start_index < total_paras:
            print(f"🔄 检测到中断的翻译进度！将自动从第 {start_index + 1} 个段落继续翻译...")
        elif start_index >= total_paras:
            print("✅ 目标文件已全部翻译完成，无需继续。")
            return

    mode = "a" if start_index > 0 else "w"
    
    with open(output_path, mode, encoding="utf-8") as f:
        for i in range(start_index, total_paras):
            para = paragraphs[i]
            para_num = i + 1
            print(f"📝 正在处理段落 {para_num}/{total_paras}...", end="\r", flush=True)
            processed = process_paragraph(para)
            prefix = "\n\n" if para_num > 1 else ""
            f.write(prefix + processed)
            f.flush()
            os.fsync(f.fileno())

    print(f"\n✅ 翻译全部完成！")
    print(f"📁 输出文件: {output_path}")

if __name__ == "__main__":
    input_file = r"path/to/your/paper.md"
    output_file = r"path/to/your/paper_bilingual.md"
    translate_markdown_robust(input_file, output_file)
```

## 输出格式示例

```markdown
# Parameterized Knowledge Transfer for Personalized Federated Learning

> # 面向个性化联邦学习的参数化知识迁移

## Abstract

> ## 摘要

In recent years, personalized federated learning...
> 近年来，个性化联邦学习...
```

## 配置参数

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `model` | doubao-seed-1-8-251228 | Doubao-Seed-1.8 模型 |
| `max_retries` | 5 | API调用重试次数 |
| `timeout` | 60.0 | API超时时间（秒） |
| `max_completion_tokens` | 65535 | 最大输出token数 |
| `reasoning_effort` | minimal | 推理努力程度 |
| `time.sleep(0.5)` | 0.5s | API调用间隔时间 |

## API调用格式

```python
response = client.chat.completions.create(
    model="doubao-seed-1-8-251228",
    max_completion_tokens=65535,
    reasoning_effort="minimal",
    messages=[
        {"role": "system", "content": system_msg},
        {"role": "user", "content": [{"type": "text", "text": text}]}
    ]
)
```

## 工作流程

1. **读取输入文件**：按 `\n\n` 分割文档为段落
2. **检测进度**：检查已有翻译，支持断点续传
3. **预处理段落**：
   - 将 LaTeX `\(\)` 替换为 `$`，`\[\]` 替换为 `$$`
   - 跳过代码块、公式块和分隔符
4. **调用API翻译**：使用火山引擎API进行翻译
5. **格式化输出**：中文翻译包裹在引用块（`> `）中
6. **实时保存**：每处理完一个段落立即写入磁盘

## 错误处理

- **API错误**：指数退避重试（2秒、4秒、8秒、16秒、32秒）
- **超时**：60秒超时后重试
- **翻译失败**：标记为 `[API连续报错...]` 并保留原文

## 最佳实践

1. **API密钥安全**：不要将API密钥提交到版本控制
2. **长文档处理**：脚本自动保存进度，支持断点续传
3. **网络稳定性**：确保网络连接稳定
4. **模型选择**：Doubao-Seed-1.8 针对学术内容进行了优化

## 故障排除

### 程序崩溃
- 检查 `translator.py` 第6行的API密钥是否有效
- 确保网络连接稳定
- 重新运行脚本，会自动从上次保存的位置继续

### 翻译质量问题
- 调整 `reasoning_effort` 参数：minimal=更快，medium/high=更 thorough
- 修改 `translate_text()` 函数中的系统提示词以适应特定领域
- 验证模型对学术内容的处理能力

### 从中断处恢复
脚本会自动检测已有的翻译进度并从中断处继续。只需重新运行：
```bash
python translator.py
```
