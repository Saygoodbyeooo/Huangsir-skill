# 📄 江西财经大学本科毕业论文排版工具

## 快速开始

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 编辑论文信息
#    打开 scripts/config.py，填写标题、姓名、学号等

# 3. 生成论文
cd scripts
python thesis_formatter.py

# 4. 打开生成的 thesis_output.docx
#    右键目录 → 更新域 → 更新整个目录
```

## 检查已有论文格式

```bash
python scripts/style_checker.py your_thesis.docx
```

## 文件说明

| 文件 | 作用 |
|------|------|
| `SKILL.md` | AI 指令规则文件 |
| `scripts/config.py` | 格式参数 + 论文信息配置 |
| `scripts/thesis_formatter.py` | 生成论文主脚本 |
| `scripts/style_checker.py` | 格式检查脚本 |

## ⚠️ 注意事项

- 生成后**必须在 Word 中更新目录域**
- 字体需系统已安装：宋体、黑体、楷体、Times New Roman
- 如需修改格式要求，只改 `scripts/config.py`