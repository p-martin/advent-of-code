#!/usr/bin/env python3


def process_content(content: str):
    jolts = [0, 0, 1]  # 1 because of the last implicit 3-jolt
    lastn = 0
    for n in sorted(map(int, content.splitlines())):
        jolts[n - lastn - 1] += 1
        lastn = n
    return jolts[0] * jolts[2]


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
