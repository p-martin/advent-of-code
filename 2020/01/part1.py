#!/usr/bin/env python3

import itertools


def process_content(content: str):
    nums = list(map(int, content.splitlines()))
    for pair in itertools.combinations(nums, 2):
        if sum(pair) == 2020:
            return pair[0] * pair[1]


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
