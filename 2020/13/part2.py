#!/usr/bin/env python3


def process_content(content: str):
    bus_ids = list(map(int, [n for n in content.splitlines()[1].replace('x', '-1').split(',')]))
    offsets = [i for i, b in enumerate(bus_ids) if b >= 0]
    bus_ids = [b for b in bus_ids if b >= 0]
    t = 0
    others = bus_ids[0]
    for b, o in zip(bus_ids[1:], offsets[1:]):
        t = calc(others, t, b, o)
        others *= b  # actually lcm, but for primes it's just others*b
    return -t


def calc(b1, o1, b2, o2):
    while o2 != o1:
        if o2 > o1:
            o2 -= (o2 - o1 + b2 - 1) // b2 * b2  # or use math.ceil
        while o1 > o2:
            o1 -= (o1 - o2 + b1 - 1) // b1 * b1
    return o1


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
