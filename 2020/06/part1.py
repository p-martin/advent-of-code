#!/usr/bin/env python3


def process_content(content: str):
    return sum([len(set(''.join(block.split())))
                for block in content.split('\n\n')])


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
