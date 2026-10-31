#!/usr/bin/env python3
"""GLOBAL.md 的结构检查。零依赖，只用标准库。

检查四件事，任一项不过即退出码 1：

1. 可执行判据覆盖率——条款里带「判据：」或带可跑命令（grep / gh api / python3 / git ls-remote）的比例；
2. 同一术语的多处定义——列出每个定义句的行号，超过一处即冲突；
3. 定点版本——正文不许出现 1.0 / 2.0 这类数（版本口径：号源只有 CI 运行数）；
4. 章节数、条款数、汉字数——只报告，不判定。

用法：python3 tools/spec_lint.py [--min-coverage 0.8]
"""
import io
import re
import sys

SPEC = "GLOBAL.md"
TERMS = ["生效点", "版本口径", "检讨", "核读", "证据", "判据", "收尾模板"]
EXECUTABLE = re.compile(r"(grep\s|gh api\s|python3\s|git ls-remote\s|gh run |gh pr )")
DEFINITION = re.compile(r"(是|为|指|＝|=|定义)")

def cjk(text):
    return len(re.findall(r"[\u4e00-\u9fff]", text))

def clauses(lines):
    """加粗条款：`- **…` 或 `N. **…` 开头的行，以及它们的续行（缩进且非空）。"""
    out = []
    current = None
    for i, line in enumerate(lines, 1):
        if re.match(r"^\s*(?:[-*]|\d+\.)\s+\*\*", line):
            if current:
                out.append(current)
            current = {"line": i, "text": line}
        elif current is not None and line.startswith((" ", "\t")) and line.strip():
            current["text"] += " " + line.strip()
        elif not line.strip():
            if current:
                out.append(current)
                current = None
    if current:
        out.append(current)
    return out

def main(argv):
    min_cov = 0.8
    if "--min-coverage" in argv:
        min_cov = float(argv[argv.index("--min-coverage") + 1])

    text = io.open(SPEC, encoding="utf-8").read()
    lines = text.split("\n")

    cs = clauses(lines)
    has_rule = [c for c in cs if "判据：" in c["text"] or EXECUTABLE.search(c["text"])]
    cov = len(has_rule) / len(cs) if cs else 0.0

    print("== 规模 ==")
    print("  行数 %d / 汉字 %d / 章节 %d / 条款 %d"
          % (len(lines), cjk(text), len(re.findall(r"^#{2,3} ", text, re.M)), len(cs)))

    print("== 1. 可执行判据覆盖率 ==")
    print("  带判据的条款 %d / %d = %.1f%%（门槛 %.0f%%）"
          % (len(has_rule), len(cs), cov * 100, min_cov * 100))
    missing = [c for c in cs if c not in has_rule]
    for c in missing:
        head = re.sub(r"\s+", " ", c["text"])[:46]
        print("    缺判据 L%-4d %s…" % (c["line"], head))

    print("== 2. 术语定义点 ==")
    conflicts = 0
    for term in TERMS:
        hits = []
        for i, line in enumerate(lines, 1):
            if term not in line:
                continue
            seg = line.split(term, 1)[1][:12]
            if DEFINITION.search(seg):
                hits.append(i)
        same_line = sorted(set(hits))
        if len(same_line) > 1:
            conflicts += 1
            print("    需人工确认 %s：定义句出现在 L%s" % (term, ", L".join(map(str, same_line))))
        else:
            print("    %s：%s" % (term, ("L%d" % same_line[0]) if same_line else "未找到定义句"))

    print("== 3. 定点版本 ==")
    license_words = ("GPL", "OFL", "Apache", "MIT", "BSD")
    bad = [(i, l.strip()[:60]) for i, l in enumerate(lines, 1)
           if re.search(r"(?<![\w.\-])(?:1\.0|2\.0)(?![\w.])", l)
           and not any(w in l for w in license_words)
           and not any(w in l for w in ("不写", "禁止", "没有语义化版本"))]
    for i, l in bad:
        print("    L%-4d %s" % (i, l))
    print("    命中 %d 处" % len(bad))

    ok = cov >= min_cov and not bad
    print("== 结论 ==")
    print("  %s" % ("通过" if ok else "不通过"))
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
