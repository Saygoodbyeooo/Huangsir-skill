"""
江西财经大学本科毕业论文格式检查工具
用法：python style_checker.py <your_thesis.docx>
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from docx import Document
from docx.shared import Pt
from docx.oxml.ns import qn

import config as cfg


class StyleChecker:
    def __init__(self, filepath):
        self.filepath = filepath
        self.doc = Document(filepath)
        self.issues = []

    def _add(self, location, expected, actual, field):
        self.issues.append({
            "location": location,
            "field": field,
            "expected": expected,
            "actual": actual,
        })

    def check_margins(self):
        for i, sec in enumerate(self.doc.sections):
            loc = f"Section {i + 1}"
            if sec.top_margin != cfg.MARGIN_TOP:
                self._add(loc, str(cfg.MARGIN_TOP), str(sec.top_margin), "上边距")
            if sec.bottom_margin != cfg.MARGIN_BOTTOM:
                self._add(loc, str(cfg.MARGIN_BOTTOM), str(sec.bottom_margin), "下边距")
            if sec.left_margin != cfg.MARGIN_LEFT:
                self._add(loc, str(cfg.MARGIN_LEFT), str(sec.left_margin), "左边距")
            if sec.right_margin != cfg.MARGIN_RIGHT:
                self._add(loc, str(cfg.MARGIN_RIGHT), str(sec.right_margin), "右边距")

    def check_fonts(self):
        for i, para in enumerate(self.doc.paragraphs):
            if para.style.name.startswith("Heading") or not para.text.strip():
                continue
            for run in para.runs:
                preview = run.text[:20] if run.text else ""
                loc = f"段落 {i + 1} ('{preview}…')"

                if run.font.size and run.font.size != cfg.BODY_SIZE:
                    self._add(loc, str(cfg.BODY_SIZE), str(run.font.size), "字号")

                if run.font.name and run.font.name != cfg.FONT_TIMES:
                    self._add(loc, cfg.FONT_TIMES, run.font.name, "英文字体")

                rpr = run._element.find(qn("w:rPr"))
                if rpr is not None:
                    rf = rpr.find(qn("w:rFonts"))
                    if rf is not None:
                        ea = rf.get(qn("w:eastAsia"))
                        allowed = [cfg.FONT_SONGTI, cfg.FONT_HEITI, cfg.FONT_KAITI]
                        if ea and ea not in allowed:
                            self._add(loc, "/".join(allowed), ea, "中文字体")

    def check_indent(self):
        for i, para in enumerate(self.doc.paragraphs):
            if para.style.name.startswith("Heading") or not para.text.strip():
                continue
            pPr = para._element.find(qn("w:pPr"))
            if pPr is not None:
                ind = pPr.find(qn("w:ind"))
                if ind is not None:
                    # 检查是否误用了固定长度缩进
                    first_line = ind.get(qn("w:firstLine"))
                    first_chars = ind.get(qn("w:firstLineChars"))
                    if first_line and not first_chars:
                        preview = para.text[:20] if para.text else ""
                        self._add(
                            f"段落 {i + 1} ('{preview}…')",
                            "w:firstLineChars=200 (2字符)",
                            f"w:firstLine={first_line} (固定长度)",
                            "首行缩进方式"
                        )

    def check_headers(self):
        for i, sec in enumerate(self.doc.sections):
            if i == 0:
                continue
            header = sec.header
            if header.paragraphs:
                text = header.paragraphs[0].text.strip()
                if i >= 2 and text and text != cfg.HEADER_TEXT:
                    self._add(f"Section {i + 1} 页眉",
                              cfg.HEADER_TEXT, text, "页眉文字")

    def run_all(self):
        print(f"🔍 正在检查：{self.filepath}")
        print("=" * 60)

        self.check_margins()
        self.check_fonts()
        self.check_indent()
        self.check_headers()

        if not self.issues:
            print("✅ 未发现格式问题！")
        else:
            print(f"⚠️  发现 {len(self.issues)} 个问题：\n")
            for i, issue in enumerate(self.issues, 1):
                print(f"  {i}. [{issue['field']}] {issue['location']}")
                print(f"     期望: {issue['expected']}")
                print(f"     实际: {issue['actual']}\n")

        print("=" * 60)
        print(f"共 {len(self.issues)} 个问题。")
        return self.issues


def main():
    if len(sys.argv) < 2:
        print("用法: python style_checker.py <your_thesis.docx>")
        sys.exit(1)
    checker = StyleChecker(sys.argv[1])
    issues = checker.run_all()
    sys.exit(1 if issues else 0)


if __name__ == "__main__":
    main()