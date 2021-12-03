#!/usr/bin/env python3


def find_value(vals, co2=False):
    for bit in range(len(vals[0])):
        cnt0 = len([0 for v in vals if v[bit] == '0'])
        cnt1 = len([1 for v in vals if v[bit] == '1'])
        want = ['1', '0'][co2] if cnt1 >= cnt0 else ['0', '1'][co2]
        vals = [v for v in vals if v[bit] == want]
        if len(vals) == 1:
            return vals[0]


def process_content(content: str):
    vals = content.splitlines()
    oxygen = find_value(vals)
    co2 = find_value(vals, True)
    return int(oxygen, 2) * int(co2, 2)


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
