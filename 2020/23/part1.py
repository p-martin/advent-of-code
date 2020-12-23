#!/usr/bin/env python3

from collections import deque


def process_content(content: str):
    cups = deque(map(int, list(content.strip())))
    for i in range(100):
        cups = move(cups)
    while cups[0] != 1:
        cups.rotate(-1)
    cups.popleft()
    return ''.join(str(n) for n in cups)


def move(cups):
    minval, maxval = min(cups), max(cups)
    cur = cups.popleft()
    picked = [cups.popleft() for __ in range(3)]
    cups.appendleft(cur)
    dest = cur
    while dest in picked + [cur]:
        dest -= 1
        if dest < minval:
            dest = maxval
    while cups[0] != dest:
        cups.rotate(-1)
    for i, p in enumerate(picked, 1):
        cups.insert(i, p)
    while cups[0] != cur:
        cups.rotate(-1)
    cups.rotate(-1)
    return cups


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
