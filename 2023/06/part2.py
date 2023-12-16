#!/usr/bin/env python3

import math


def process_content(content: str):
    lines = content.splitlines()
    t = int(lines[0].split(":")[1].replace(" ", ""))
    d = int(lines[1].split(":")[1].replace(" ", ""))

    return sum(ms*(t-ms) > d for ms in range(t))


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
