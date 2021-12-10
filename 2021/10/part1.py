#!/usr/bin/env python3


def check(line):
    braces = []
    for c in line:
        if c in '{([<':
            braces.append(c)
        elif braces and braces[-1] == {')':'(', ']':'[', '}':'{', '>':'<'}[c]:
            braces.pop()
        else:
            return {')': 3, ']': 57, '}': 1197, '>': 25137}[c]
    return 0


def process_content(content: str):
    return sum(check(line)
               for line in content.splitlines())


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
