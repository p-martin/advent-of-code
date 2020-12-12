#!/usr/bin/env python3


def process_content(content: str):
    content = content.replace('L', '#')
    changed = True
    while changed:
        content, changed = calc(content)
    return content.count('#')


def calc(content):
    changed = False
    newLines = [list(l) for l in content.splitlines()]
    lines = content.splitlines()
    for y, line in enumerate(lines):
        for x, seat in enumerate(line):
            if seat == '.':
                continue
            else:
                occ = 0
                for dx, dy in [(-1, -1), (0, -1), (1, -1),
                               (-1, 0), (1, 0),
                               (-1, 1), (0, 1), (1, 1)]:
                    tx, ty = x + dx, y + dy
                    if 0 <= ty < len(lines) and 0 <= tx < len(line):
                        if lines[ty][tx] == '#':
                            occ += 1
                if seat == '#' and occ >= 4:
                    newLines[y][x] = 'L'
                    changed = True
                elif seat == 'L' and occ == 0:
                    newLines[y][x] = '#'
                    changed = True
    return '\n'.join(''.join(l) for l in newLines), changed



if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
