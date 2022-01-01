#!/usr/bin/env python3


def process_content(content: str):
    lines = content.splitlines()
    width, height = len(lines[0]), len(lines)

    east = {(x, y) for y, line in enumerate(lines) for x, c in enumerate(line) if c == '>'}
    south = {(x, y) for y, line in enumerate(lines) for x, c in enumerate(line) if c == 'v'}

    step, changed = 0, True
    while changed:
        step += 1
        changed = False

        neweast = set()
        for x, y in east:
            tx = (x + 1) % width
            if (tx, y) not in east and (tx, y) not in south:
                neweast.add((tx, y))
                changed = True
            else:
                neweast.add((x, y))
        east = neweast

        newsouth = set()
        for x, y in south:
            ty = (y + 1) % height
            if (x, ty) not in east and (x, ty) not in south:
                newsouth.add((x, ty))
                changed = True
            else:
                newsouth.add((x, y))
        south = newsouth

    return step


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
