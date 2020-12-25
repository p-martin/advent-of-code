#!/usr/bin/env python3


def process_content(content: str):
    flipped = set()
    for line in content.splitlines():
        x = y = 0
        while line:
            direction, line = line[0], line[1:]
            x += {'e': 1, 'w': -1}.get(direction, 0)
            if direction in 'ns':
                y += {'n': -1, 's': 1}.get(direction, 0)
                direction, line = line[0], line[1:]
                x += [{'e': 1}, {'w': -1}][y % 2].get(direction, 0)
        if (x, y) in flipped:
            flipped.remove((x, y))
        else:
            flipped.add((x, y))
    return len(flipped)


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
