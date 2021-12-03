#!/usr/bin/env python3


def process_content(content: str):
    vals = content.splitlines()
    gamma = ''
    epsilon = ''
    for bit in range(len(vals[0])):
        cnt0 = len([0 for v in vals if v[bit] == '0'])
        cnt1 = len([1 for v in vals if v[bit] == '1'])
        gamma += '1' if cnt1 > cnt0 else '0'
        epsilon += '0' if cnt1 > cnt0 else '1'
    return int(gamma, 2) * int(epsilon, 2)


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
