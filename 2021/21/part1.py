#!/usr/bin/env python3


def process_content(content: str):
    p1, p2 = [int(line.split(': ')[-1])
              for line in content.strip().splitlines()]

    sc1, sc2, roll, d = 0, 0, 0, 0
    while True:
        for i in range(3):
            roll, d = roll+1, d+1
            p1 = (p1 + d - 1) % 10 + 1
        sc1 += p1
        if sc1 >= 1000:
            return sc2 * roll

        for i in range(3):
            roll, d = roll+1, d+1
            p2 = (p2 + d - 1) % 10 + 1
        sc2 += p2
        if sc2 >= 1000:
            return sc1 * roll


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
