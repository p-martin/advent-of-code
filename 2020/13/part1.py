#!/usr/bin/env python3


def process_content(content: str):
    lines = content.splitlines()
    ts = int(lines[0])
    bus_ids = list(map(int, [n for n in lines[1].split(',') if n != 'x']))
    waits = {b - ts % b: b
             for b in bus_ids}
    first = min(waits.keys())
    return first * waits[first]


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
