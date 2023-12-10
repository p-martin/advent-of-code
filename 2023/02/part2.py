#!/usr/bin/env python3

import math


def process_content(content: str):
    res = 0
    for line in content.strip().splitlines():
        d = {}
        for draw in line.split(":")[-1].split(";"):
            for n, color in map(str.split, draw.split(",")):
                d[color] = max(d.get(color, 0), int(n))
        res += math.prod(d.values())
    return res


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
