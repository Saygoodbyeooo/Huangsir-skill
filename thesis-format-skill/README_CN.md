# 📄 江西财经大学现代经济管理学院本科毕业论文排版工具

## 快速开始

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 编辑 scripts/config.py 填写论文信息

# 3. 生成论文
cd scripts
python thesis_formatter.py

# 4. 打开生成的 thesis_output.docx
#    Ctrl+A 全选 → F9 更新域（生成目录）
```

## 检查格式

```bash
python scripts/style_checker.py your_thesis.docx
```

## ⚠️ 注意

- 生成后**必须在 Word 中按 Ctrl+A → F9 更新目录**
- 系统需安装字体：宋体、黑体、楷体、Times New Roman