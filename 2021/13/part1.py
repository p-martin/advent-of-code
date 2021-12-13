#!/usr/bin/env python3


def process_content(content: str):
    coords, instructions = content.split('\n\n')
    coords = {tuple(map(int, line.split(',')))
              for line in coords.splitlines()}

    d, val = instructions.splitlines()[0].rsplit()[-1].split('=')
    val = int(val)
    if d == 'x':
        coords = {(2*val-x, y) if x >= val else (x, y)
                  for x, y in coords}
    else:
        coords = {(x, 2*val-y) if y >= val else (x, y)
                  for x, y in coords}

    return len(coords)


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
