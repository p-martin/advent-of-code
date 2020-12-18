#!/usr/bin/env python3

import re


class MyInt:
    def __init__(self, val):
        self.val = val

    # use Python's operator precedence, but perform the other operation
    def __add__(self, other):
        return MyInt(self.val * other.val)

    def __mul__(self, other):
        return MyInt(self.val + other.val)


def process_content(content: str):
    return sum(calc(line)
               for line in content.splitlines())


def calc(line):
    return eval(re.sub(r'(\d+)', r'MyInt(\1)',
                       line.translate({ord('+'): '*', ord('*'): '+'}))).val


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
