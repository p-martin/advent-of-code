#!/usr/bin/env python3


def process_content(content: str):
    pks = list(map(int, content.splitlines()))
    ls = {}
    sn, value = 7, 1
    i = 1
    while True:
        value = (value * sn) % 20201227
        if value in pks:
            ls[value] = i
            if len(ls) == 2:
                break
        i += 1
    sn, value = pks[0], 1
    for i in range(ls[pks[1]]):
        value = (value * sn) % 20201227
    return value


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
