#!/usr/bin/env python3
"""本庫輕量結構檢查：目錄名＝frontmatter name、description_zh 存在、本地連結可解析。"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FAIL = []


def check_tree(base: str) -> int:
    n = 0
    root = ROOT / base
    if not root.exists():
        return 0
    for d in sorted(root.iterdir()):
        if not d.is_dir() or d.name.startswith('.'):
            continue
        f = d / 'SKILL.md'
        if not f.exists():
            FAIL.append(f'{base}/{d.name}: 缺 SKILL.md')
            continue
        text = f.read_text(encoding='utf-8')
        m = re.match(r'^---\n(.*?)\n---\n', text, re.S)
        if not m:
            FAIL.append(f'{base}/{d.name}: 無 YAML frontmatter')
            continue
        front = m.group(1)
        mn = re.search(r'^name:\s*(\S+)', front, re.M)
        if not mn or mn.group(1) != d.name:
            FAIL.append(f'{base}/{d.name}: name 與目錄名不一致')
        if 'description:' not in front:
            FAIL.append(f'{base}/{d.name}: 缺 description')
        if 'description_zh:' not in front:
            FAIL.append(f'{base}/{d.name}: 缺 description_zh')
        # 本地連結檢查（references/、assets/、scripts/）；略過 url 佔位範例
        for link in re.findall(r'\]\(([^)http][^)]*)\)', text):
            if link.strip() == 'url':
                continue
            target = (d / link.split('#')[0]).resolve()
            if not target.exists():
                FAIL.append(f'{base}/{d.name}: 連結失效 {link}')
        n += 1
    return n


if __name__ == '__main__':
    a = check_tree('skills')
    b = check_tree('skills-tw')
    print(f'skills: {a}, skills-tw: {b}')
    if FAIL:
        print('FAIL:')
        for x in FAIL:
            print(' -', x)
        sys.exit(1)
    print('PASS')
