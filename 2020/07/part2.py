#!/usr/bin/env python3

import re


def process_content(content: str):
    d = {}
    for line in content.splitlines():
        k, v = line.split(' contain ')
        d[k.rsplit(None, 1)[0]] = [vv.rsplit(None, 1)[0]
                                   for vv in v.split(', ')]
    return calc(d, 'shiny gold') - 1  # don't count shiny gold itself


def calc(d, color):
    r = 1
    for vv in d[color]:
        if vv == 'no other':
            continue
        num, color2 = vv.split(None, 1)
        r += int(num) * calc(d, color2)
    return r


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
