# 🧠 My Skills

个人 AI Skill 库 —— 一系列可复用的 AI 指令集，配合 Cursor / Trae / Copilot 等工具使用。

## 📦 Skill 列表

| Skill | 说明 | 状态 |
|-------|------|------|
| [thesis-format](./thesis-format/) | 江西财经大学现代经济管理学院本科毕业论文 DOCX 自动排版 | ✅ 可用 |
| code-review | 代码审查规范 | 🚧 计划中 |
| api-design | REST API 设计规范 | 🚧 计划中 |

## 🚀 如何使用

### 方式 1：在 AI IDE 中使用（推荐）

1. Clone 本仓库：
```bash
git clone https://github.com/Saygoodbyeooo/my-skills.git
```

2. 根据你的工具，将对应 Skill 的 `SKILL.md` 复制到规则目录：

| 工具 | 复制到 |
|------|--------|
| Cursor | `.cursor/rules/<skill-name>.md` |
| Windsurf | `.windsurf/rules/<skill-name>.md` |
| Cline | `.clinerules/<skill-name>.md` |
| Trae | 在对话中引用 `SKILL.md` |
| Copilot | `.github/copilot-instructions.md` |

3. 在对话中告诉 AI："请按照 SKILL.md 的规范执行"

### 方式 2：直接运行脚本

```bash
cd thesis-format/scripts
pip install -r ../requirements.txt
python thesis_formatter.py
```

## 📝 如何添加新 Skill

1. 在根目录创建新文件夹（如 `new-skill/`）
2. 至少包含一个 `SKILL.md`（核心指令文件）
3. 如有脚本，放在 `scripts/` 子目录
4. 更新本 README 的 Skill 列表

## 📁 标准 Skill 结构

```
skill-name/
├── SKILL.md            ← 必须：AI 指令定义
├── README.md           ← 推荐：人类可读的说明
├── requirements.txt    ← 可选：Python 依赖
└── scripts/            ← 可选：执行脚本
    └── ...
```
