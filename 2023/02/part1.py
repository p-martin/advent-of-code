#!/usr/bin/env python3


def process_content(content: str):
    res = 0
    for line in content.strip().splitlines():
        if all(int(n) <= {"red": 12, "green": 13, "blue": 14}[color]
               for draw in line.split(":")[-1].split(";")
               for n, color in map(str.split, draw.split(","))):
            res += int(line.split(":")[0].split()[-1])
    return res


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
