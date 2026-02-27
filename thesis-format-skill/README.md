# 📄 JXUFE Undergraduate Thesis DOCX Formatter

Automatically generates Word documents conforming to the Jiangxi University of Finance and Economics (JXUFE) undergraduate thesis formatting guidelines.

## ✨ Features

- ✅ One-click generation of complete thesis structure
- ✅ Strict compliance with JXUFE formatting standards
- ✅ Automatic Roman/Arabic page number switching
- ✅ Auto-configured headers and footers
- ✅ TOC field code for Word auto-generation
- ✅ Style checker for existing documents
- ✅ Correct CJK first-line indent (character-based, not cm/pt)

## 📦 Installation

```bash
pip install python-docx
```

## 🚀 Usage

### Generate Thesis

1. Edit `scripts/config.py` with your thesis information
2. Run: `cd scripts && python thesis_formatter.py`
3. Open the generated `.docx` and update the TOC field in Word

### Check Formatting

```bash
python scripts/style_checker.py your_thesis.docx
```

## 📁 Structure

```
thesis-format-skill/
├── SKILL.md
├── README.md
├── README_CN.md
├── requirements.txt
└── scripts/
    ├── config.py
    ├── thesis_formatter.py
    └── style_checker.py
```

## 📋 Formatting Source

JXUFE Undergraduate Thesis Writing Guidelines (《江西财经大学普通本科毕业论文指导手册》)