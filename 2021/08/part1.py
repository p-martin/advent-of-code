#!/usr/bin/env python3


def process_content(content: str):
    return len([1
                for line in content.splitlines()
                for digit in line.split(' | ')[-1].split()
                if len(digit) in (2, 4, 3, 7)])


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
