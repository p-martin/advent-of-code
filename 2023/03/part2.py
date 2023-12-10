#!/usr/bin/env python3

import math


def process_content(content: str):
    res = 0
    lines = content.splitlines()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "*":
                gear = {}
                for ty in range(max(0, y-1), min(len(lines), y+2)):
                    for dx in (-1, 0, 1):
                        fx = tx = x+dx
                        if 0 <= fx < len(lines[ty]) and lines[ty][fx].isdigit():
                            while fx > 0 and lines[ty][fx-1].isdigit():
                                fx -= 1
                            while tx < len(lines[ty])-1 and lines[ty][tx+1].isdigit():
                                tx += 1
                            gear[(fx, ty)] = int(lines[ty][fx:tx+1])
                if len(gear) > 1:
                    res += math.prod(gear.values())
    return res


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
