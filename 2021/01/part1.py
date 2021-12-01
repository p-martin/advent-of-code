#!/usr/bin/env python3


def process_content(content: str):
    ints = list(map(int, content.splitlines()))
    return len([1
                for a, b in zip(ints, ints[1:])
                if a < b])


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
