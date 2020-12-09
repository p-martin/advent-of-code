#!/usr/bin/env python3

import itertools


def process_content(content: str):
    nums = list(map(int, content.splitlines()))
    for i, n in enumerate(nums):
        if i >= 25:
            if any(a != b and a + b == n
                   for a, b in itertools.combinations(nums[i-25:i], 2)):
                continue
            return n


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
