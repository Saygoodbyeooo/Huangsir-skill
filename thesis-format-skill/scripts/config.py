"""
江西财经大学本科毕业论文格式配置
所有格式参数集中管理，修改格式只需改此文件
"""

from docx.shared import Pt, Cm


# ============================================================
# 封面信息（用户必填）
# ============================================================
SCHOOL_NAME = "江西财经大学"
THESIS_TYPE = "普通本科毕业论文"
TITLE = "基于XXX的XXX系统设计与实现"
SUBTITLE = ""
STUDENT_NAME = "张三"
STUDENT_ID = "2022XXXXXX"
DEPARTMENT = "计算机科学与技术学院"
MAJOR = "软件工程"
ADVISOR = "李四 教授"
DATE = "2026年6月"


# ============================================================
# 页面设置
# ============================================================
PAGE_WIDTH = Cm(21.0)
PAGE_HEIGHT = Cm(29.7)
MARGIN_TOP = Cm(2.54)
MARGIN_BOTTOM = Cm(2.54)
MARGIN_LEFT = Cm(3.17)
MARGIN_RIGHT = Cm(3.17)


# ============================================================
# 字体名称
# ============================================================
FONT_SONGTI = "宋体"
FONT_HEITI = "黑体"
FONT_KAITI = "楷体"
FONT_TIMES = "Times New Roman"


# ============================================================
# 字号映射（中国字号 → pt）
# ============================================================
SIZE_SANHAO = Pt(16)       # ���号
SIZE_XIAOSAN = Pt(15)      # 小三号
SIZE_SIHAO = Pt(14)        # 四号
SIZE_XIAOSI = Pt(12)       # 小四号
SIZE_WUHAO = Pt(10.5)      # 五号
SIZE_XIAOWU = Pt(9)        # 小五号


# ============================================================
# 行距
# ============================================================
LINE_SPACING_22PT = Pt(22)
LINE_SPACING_18PT = Pt(18)
LINE_SPACING_1_5 = 1.5


# ============================================================
# 首行缩进（字符数，用于 w:firstLineChars）
# ============================================================
FIRST_LINE_INDENT_CHARS = 2.0   # 2 字符


# ============================================================
# 页眉
# ============================================================
HEADER_TEXT = "江西财经大学普通本科毕业论文"
HEADER_FONT = FONT_SONGTI
HEADER_FONT_SIZE = SIZE_WUHAO


# ============================================================
# 摘要部分
# ============================================================
ABSTRACT_TITLE_CN = "摘要"
ABSTRACT_TITLE_EN = "Abstract"
ABSTRACT_TITLE_FONT_CN = FONT_HEITI
ABSTRACT_TITLE_FONT_EN = FONT_TIMES
ABSTRACT_TITLE_SIZE = SIZE_XIAOSAN

ABSTRACT_BODY_FONT_CN = FONT_KAITI
ABSTRACT_BODY_FONT_EN = FONT_TIMES
ABSTRACT_BODY_SIZE = SIZE_XIAOSI
ABSTRACT_LINE_SPACING = LINE_SPACING_22PT

KEYWORD_LABEL_CN = "【关键词】"
KEYWORD_LABEL_EN = "【Key words】"
KEYWORD_LABEL_FONT_CN = FONT_HEITI
KEYWORD_LABEL_FONT_EN = FONT_TIMES
KEYWORD_LABEL_SIZE = SIZE_XIAOSI
KEYWORD_BODY_FONT_CN = FONT_KAITI
KEYWORD_BODY_FONT_EN = FONT_TIMES


# ============================================================
# 目录部分
# ============================================================
TOC_TITLE = "目录"
TOC_TITLE_FONT = FONT_HEITI
TOC_TITLE_SIZE = SIZE_XIAOSAN


# ============================================================
# 正文标题
# ============================================================
BODY_TITLE_FONT = FONT_SONGTI
BODY_TITLE_SIZE = SIZE_SANHAO
BODY_TITLE_BOLD = True

HEADING1_FONT = FONT_SONGTI
HEADING1_SIZE = SIZE_XIAOSAN
HEADING1_BOLD = True
HEADING1_LINE_SPACING = LINE_SPACING_1_5
HEADING1_SPACE_BEFORE = Pt(7.8)    # 约 0.5 行
HEADING1_SPACE_AFTER = Pt(7.8)

HEADING2_FONT = FONT_SONGTI
HEADING2_SIZE = SIZE_SIHAO
HEADING2_BOLD = True
HEADING2_LINE_SPACING = LINE_SPACING_1_5
HEADING2_SPACE_BEFORE = Pt(0)
HEADING2_SPACE_AFTER = Pt(0)

HEADING3_FONT = FONT_SONGTI
HEADING3_SIZE = SIZE_XIAOSI
HEADING3_BOLD = True
HEADING3_LINE_SPACING = LINE_SPACING_1_5
HEADING3_SPACE_BEFORE = Pt(0)
HEADING3_SPACE_AFTER = Pt(0)


# ============================================================
# 正文
# ============================================================
BODY_FONT_CN = FONT_SONGTI
BODY_FONT_EN = FONT_TIMES
BODY_SIZE = SIZE_XIAOSI
BODY_LINE_SPACING = LINE_SPACING_22PT
BODY_SPACE_BEFORE = Pt(0)
BODY_SPACE_AFTER = Pt(0)


# ============================================================
# 参考文献
# ============================================================
REF_TITLE = "参考文献"
REF_FONT_CN = FONT_SONGTI
REF_FONT_EN = FONT_TIMES
REF_SIZE = SIZE_WUHAO
REF_LINE_SPACING = LINE_SPACING_18PT


# ============================================================
# 致谢
# ============================================================
THANKS_TITLE = "致谢"
THANKS_FONT = FONT_SONGTI
THANKS_SIZE = SIZE_XIAOSI
THANKS_LINE_SPACING = LINE_SPACING_22PT


# ============================================================
# 默认章节骨架
# ============================================================
DEFAULT_CHAPTERS = [
    {
        "number": "1",
        "title": "绪论",
        "sections": [
            {"number": "1.1", "title": "研究背景", "body": "在此填写研究背景内容……"},
            {"number": "1.2", "title": "研究目的与意义", "body": "在此填写研究目的与意义……"},
            {"number": "1.3", "title": "国内外研究现状", "body": "在此填写国内外研究现状……"},
            {"number": "1.4", "title": "论文组织结构", "body": "在此填写论文组织结构说明……"},
        ],
    },
    {
        "number": "2",
        "title": "相关技术与理论基础",
        "sections": [
            {"number": "2.1", "title": "XXX技术", "body": "在此填写相关技术介绍……"},
            {"number": "2.2", "title": "YYY理论", "body": "在此填写理论基础……"},
        ],
    },
    {
        "number": "3",
        "title": "系统需求分析",
        "sections": [
            {"number": "3.1", "title": "功能需求", "body": "在此填写功能需求分析……"},
            {"number": "3.2", "title": "非功能需求", "body": "在此填写非功能需求……"},
        ],
    },
    {
        "number": "4",
        "title": "系统设计",
        "sections": [
            {"number": "4.1", "title": "总体架构设计", "body": "在此填写系统总体架构……"},
            {"number": "4.2", "title": "数据库设计", "body": "在此填写数据库表结构设计……"},
            {"number": "4.3", "title": "接口设计", "body": "在此填写API/接口设计……"},
        ],
    },
    {
        "number": "5",
        "title": "系统实现",
        "sections": [
            {"number": "5.1", "title": "开发环境", "body": "在此填写开发环境与工具……"},
            {"number": "5.2", "title": "核心模块实现", "body": "在此填写核心功能实现细节……"},
        ],
    },
    {
        "number": "6",
        "title": "系统测试",
        "sections": [
            {"number": "6.1", "title": "测试环境", "body": "在此填写测试环境……"},
            {"number": "6.2", "title": "功能测试", "body": "在此填写功能测试用例与结果……"},
            {"number": "6.3", "title": "性能测试", "body": "在此填写性能测试结果……"},
        ],
    },
    {
        "number": "7",
        "title": "总结与展望",
        "sections": [
            {"number": "7.1", "title": "工作总结", "body": "在此填写论文工作总结……"},
            {"number": "7.2", "title": "不足与展望", "body": "在此填写不足之处及未来工作方向……"},
        ],
    },
]