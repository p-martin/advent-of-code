#!/usr/bin/env python3


def process_content(content: str):
    ints = [[(int(digit) + x + y - 1) % 9 + 1
             for x in range(5)
             for digit in line]
            for y in range(5)
            for line in content.splitlines()]

    target_x, target_y = len(ints[0]) - 1, len(ints) - 1
    risks = {(0, 0): 0}

    ff = {(0, 0)}
    while ff:
        newff = set()
        for x, y in ff:
            r = risks[(x, y)]
            for dx, dy in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
                tx, ty = x + dx, y + dy
                if (0 <= tx <= target_x and 0 <= ty <= target_y and
                        ((tx, ty) not in risks or risks[(tx, ty)] > r + ints[ty][tx])):
                    risks[(tx, ty)] = r + ints[ty][tx]
                    newff.add((tx, ty))
        ff = newff

    return risks[(target_x, target_y)]


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
