#!/usr/bin/env python3


def process_content(content: str):
    x = y = 0
    facing = 'E'
    for mv in content.splitlines():
        act, val = mv[0], int(mv[1:])
        x += {'E': val, 'W': -val}.get(act, 0)
        y += {'N': -val, 'S': val}.get(act, 0)
        if act == 'F':
            x += {'E': val, 'W': -val}.get(facing, 0)
            y += {'N': -val, 'S': val}.get(facing, 0)
        elif act == 'L':
            for __ in range(val // 90):
                facing = {'E': 'N', 'N': 'W', 'W': 'S', 'S': 'E'}[facing]
        elif act == 'R':
            for __ in range(val // 90):
                facing = {'E': 'S', 'S': 'W', 'W': 'N', 'N': 'E'}[facing]
    return abs(x) + abs(y)


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
