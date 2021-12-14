#!/usr/bin/env python3

from collections import Counter


def process_content(content: str):
    poly, rules = content.split('\n\n')
    for i in range(10):
        newpoly = []
        for j, pair in enumerate(zip(poly[:-1], poly[1:])):
            for r in rules.splitlines():
                rpair, rinsert = r.split(' -> ')
                if ''.join(pair) == rpair:
                    newpoly.append((rpair[0] + rinsert + rpair[1])
                                   if j == 0
                                   else (rinsert + rpair[1]))
        poly = ''.join(newpoly)

    q = Counter(poly)
    return max(q.values()) - min(q.values())


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
