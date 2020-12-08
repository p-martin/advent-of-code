#!/usr/bin/env python3


def process_content(content: str):
    return sum([calc_value(block)
                for block in content.split('\n\n')])


def calc_value(block):
    lines = block.splitlines()
    s = set(lines[0])
    for line in lines[1:]:
        s = s.intersection(set(line))
    return len(s)


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
