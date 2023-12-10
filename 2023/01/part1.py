#!/usr/bin/env python3

import re


def process_content(content: str):
    res = 0
    for line in content.strip().splitlines():
        a = int(re.search(r"(\d)", line).group(1))
        b = int(re.search(r"(\d)", line[::-1]).group(1))
        res += a*10 + b
    return res


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
