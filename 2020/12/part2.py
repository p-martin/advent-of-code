#!/usr/bin/env python3


def process_content(content: str):
    x = y = 0
    wp = [10, -1]
    for mv in content.splitlines():
        act, val = mv[0], int(mv[1:])
        wp[0] += {'E': val, 'W': -val}.get(act, 0)
        wp[1] += {'N': -val, 'S': val}.get(act, 0)
        if act == 'F':
            x += val * wp[0]
            y += val * wp[1]
        elif act == 'L':
            for __ in range(val // 90):
                wp = [wp[1], -wp[0]]
        elif act == 'R':
            for __ in range(val // 90):
                wp = [-wp[1], wp[0]]
    return abs(x) + abs(y)


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
