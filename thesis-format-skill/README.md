# 📄 JXUFE Undergraduate Thesis DOCX Formatter

Automatically generates Word documents conforming to the Jiangxi University of Finance and Economics (JXUFE) Modern Economics and Management College undergraduate thesis formatting guidelines.

## 📦 Installation

```bash
pip install python-docx
```

## 🚀 Usage

1. Edit `scripts/config.py` with your thesis information
2. Run: `cd scripts && python thesis_formatter.py`
3. Open the generated `.docx` in Word → Ctrl+A → F9 to update TOC

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