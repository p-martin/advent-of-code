#!/usr/bin/env python3

from functools import lru_cache
from itertools import product


@lru_cache(200000)
def get_num_wins(sc1, sc2, p1, p2):
    if sc2 >= 21:
        return 0, 1
    w1 = w2 = 0
    for dicevals in product((1, 2, 3), repeat=3):
        newp1 = (p1 - 1 + sum(dicevals)) % 10 + 1
        newsc1 = sc1 + newp1
        nw2, nw1 = get_num_wins(sc2, newsc1, p2, newp1)
        w1, w2 = w1+nw1, w2+nw2
    return w1, w2


def process_content(content: str):
    p1, p2 = [int(line.split(': ')[-1])
              for line in content.strip().splitlines()]

    return max(get_num_wins(0, 0, p1, p2))


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
