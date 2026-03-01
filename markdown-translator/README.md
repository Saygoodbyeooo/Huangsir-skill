# Markdown 学术论文翻译工具

> Markdown Academic Paper Translator

使用火山引擎 API 将英文 Markdown 格式的学术论文翻译成中文双语对照文档。

---

## 📋 目录

- [功能特点](#功能特点)
- [快速开始](#快速开始)
- [安装依赖](#安装依赖)
- [使用方法](#使用方法)
- [配置说明](#配置说明)
- [输出格式](#输出格式)
- [常见问题](#常见问题)
- [更新日志](#更新日志)

---

## ✨ 功能特点

- 🔄 **双语对照输出**：英文原文 + 中文翻译（引用块格式）
- 🧮 **LaTeX公式保留**：保持所有数学公式不变
- 📝 **Markdown格式保留**：保持标题、加粗、列表等格式
- 🖼️ **图片路径保留**：图片路径不变，仅翻译说明文字
- ⏯️ **断点续传**：支持中断后继续翻译
- 🔄 **错误重试**：指数退避重试机制

---

## 🚀 快速开始

### 1. 克隆或下载项目

```bash
cd translator_v1
```

### 2. 安装依赖

```bash
pip install openai
```

### 3. 配置API密钥

编辑 `translator.py` 文件，第6行填入你的火山引擎API密钥：

```python
api_key = "你的API密钥"
```

### 4. 配置输入输出文件

编辑 `translator.py` 文件，第152-153行：

```python
input_file = r"path/to/your/paper.md"
output_file = r"path/to/your/paper_bilingual.md"
```

### 5. 运行翻译

```bash
python translator.py
```

---

## 📦 安装依赖

### 必需依赖

```bash
pip install openai
```

### 可选依赖（用于PDF转换）

```bash
pip install markdown fpdf2
```

---

## 📖 使用方法

### 基本用法

```bash
python translator.py
```

程序会自动：
1. 读取输入的 Markdown 文件
2. 检测已有翻译进度
3. 逐段翻译并生成双语对照
4. 实时保存到输出文件

### 命令行参数

目前不支持命令行参数，需要直接在脚本中修改输入输出路径。

### 从中断处恢复

如果翻译过程中断，只需重新运行：

```bash
python translator.py
```

程序会自动检测已有进度并从中断处继续翻译。

---

## ⚙️ 配置说明

### API配置

| 配置项 | 默认值 | 说明 |
|--------|--------|------|
| `api_key` | - | 火山引擎API密钥（必填） |
| `base_url` | `https://ark.cn-beijing.volces.com/api/v3` | 火山引擎API地址 |
| `timeout` | 60.0 | API请求超时时间（秒） |

### 模型配置

| 配置项 | 默认值 | 说明 |
|--------|--------|------|
| `model` | `doubao-seed-1-8-251228` | 使用的AI模型 |
| `max_completion_tokens` | 65535 | 最大输出token数 |
| `reasoning_effort` | `minimal` | 推理努力程度 |
| `temperature` | - | 温度参数（通过系统提示控制） |

### 翻译配置

| 配置项 | 默认值 | 说明 |
|--------|--------|------|
| `max_retries` | 5 | API调用失败重试次数 |
| `time.sleep(0.5)` | 0.5秒 | API调用间隔时间 |

---

## 📄 输出格式

### 双语对照格式

```markdown
# 英文标题

> # 中文标题

英文段落内容...

> 中文翻译内容...

## 英文二级标题

> ## 中文二级标题
```

### 特点

- 英文原文保持原有格式
- 中文翻译使用引用块（`> `）包裹
- 引用块在Markdown渲染器中显示为灰色背景
- 便于对照阅读

---

## ❓ 常见问题

### Q1: 如何获取火山引擎API密钥？

A1: 访问 [火山引擎方舟平台](https://console.volcengine.com/ark/)，注册账号并创建API密钥。

### Q2: 翻译过程中断怎么办？

A2: 直接重新运行 `python translator.py`，程序会自动从中断处继续翻译。

### Q3: 支持哪些模型？

A3: 当前配置使用 `doubao-seed-1-8-251228`（Doubao-Seed-1.8）模型，针对学术内容进行了优化。

### Q4: 翻译质量如何调整？

A4: 可以调整 `reasoning_effort` 参数：
- `minimal`：速度最快
- `medium`：平衡速度和质量
- `high`：质量最高但速度较慢

### Q5: 支持其他语言吗？

A5: 当前版本专门针对英译中优化，如需其他语言组合，需要修改系统提示词。

### Q6: 如何处理LaTeX公式？

A6: 程序会自动：
- 将 `\(\)` 替换为 `$`
- 将 `\[\]` 替换为 `$$`
- 保持公式内容不翻译

---

## 📝 更新日志

### v1.0.0 (2026-03-01)

- ✅ 初始版本发布
- ✅ 支持火山引擎API
- ✅ 实现双语对照输出
- ✅ 支持断点续传
- ✅ 添加指数退避重试机制
- ✅ 支持LaTeX公式保留
- ✅ 添加中文README文档

---

## 🤝 贡献

欢迎提交Issue和Pull Request！

## 📄 许可证

MIT License

---

## 📧 联系方式

如有问题，请通过以下方式联系：
- 提交GitHub Issue
- 发送邮件至：your-email@example.com

---

**Made with ❤️ for academic paper translation**
