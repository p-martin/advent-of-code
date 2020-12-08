#!/usr/bin/env python3


def process_content(content: str):
    return len([line
                for line in content.splitlines()
                if is_valid(line)])


def is_valid(line):
    g, G, c, p = line.replace('-', ' ').replace(':', '').split()
    c1, c2 = p[int(g) - 1], p[int(G) - 1]
    return c in (c1, c2) and c1 != c2


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
