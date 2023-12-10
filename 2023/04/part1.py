#!/usr/bin/env python3


def process_content(content: str):
    res = 0
    for line in content.splitlines():
        a, b = line.split(": ")[1].split(" | ")
        wc = len(set(map(int, a.split())).intersection(map(int, b.split())))
        res += int(2**(wc-1))
    return res


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
