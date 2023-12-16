#!/usr/bin/env python3

from collections import Counter
from functools import cmp_to_key

ST = "AKQJT98765432"


def gettype(c):
    cnt = Counter(c)
    if len(cnt) == 1:
        return 7  # 5 of a kind
    if len(cnt) == 2:
        if 4 in cnt.values():
            return 6  # 4 of a kind
        return 5  # full house
    if 3 in cnt.values():
        return 4  # 3 of a kind
    if Counter(cnt.values()).get(2) == 2:
        return 3  # 2 pair
    if Counter(cnt.values()).get(2) == 1:
        return 2  # 1 pair
    if len(cnt) == 5:
        return 1  # high card
    assert 0, c  # shouldn't exist


def cmp(a, b):
    ta, tb = gettype(a), gettype(b)
    if ta != tb:
        return -1 if ta < tb else 1
    for ca, cb in zip(a, b):
        ia, ib = ST.index(ca), ST.index(cb)
        if ia != ib:
            return 1 if ia < ib else -1
    return 0


def process_content(content: str):
    hands = []
    for line in content.splitlines():
        cards, bid = line.split()
        hands.append((cards, int(bid)))
    hands.sort(key=cmp_to_key(lambda a, b: cmp(a[0], b[0])))

    return sum(n * r[1] for n, r in enumerate(hands, 1))


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
