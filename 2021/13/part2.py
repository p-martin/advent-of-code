#!/usr/bin/env python3


def process_content(content: str):
    coords, instructions = content.split('\n\n')
    coords = {tuple(map(int, line.split(',')))
              for line in coords.splitlines()}

    for instr in instructions.splitlines():
        d, val = instr.rsplit()[-1].split('=')
        val = int(val)
        if d == 'x':
            coords = {(2*val-x, y) if x >= val else (x, y)
                      for x, y in coords}
        else:
            coords = {(x, 2*val-y) if y >= val else (x, y)
                      for x, y in coords}

    minx, maxx = min(x for x, y in coords), max(x for x, y in coords)
    miny, maxy = min(y for x, y in coords), max(y for x, y in coords)
    return '\n' + '\n'.join(''.join('#' if (x, y) in coords else '.'
                                    for x in range(minx, maxx+1))
                            for y in range(miny, maxy+1))


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {result}')
