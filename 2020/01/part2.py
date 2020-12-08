#!/usr/bin/env python3

import itertools


def process_content(content: str):
    nums = list(map(int, content.splitlines()))
    for triple in itertools.combinations(nums, 3):
        if sum(triple) == 2020:
            return triple[0] * triple[1] * triple[2]


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
