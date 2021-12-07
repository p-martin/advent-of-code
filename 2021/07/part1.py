#!/usr/bin/env python3


def process_content(content: str):
    ints = list(map(int, content.split(',')))
    fuels = []
    for p in range(min(ints), max(ints)+1):
        fuels.append(sum(abs(n - p) for n in ints))
    return min(fuels)


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
