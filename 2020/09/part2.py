#!/usr/bin/env python3

import itertools


def process_content(content: str):
    nums = list(map(int, content.splitlines()))
    for i, n in enumerate(nums):
        if i >= 25:
            if any(a != b and a + b == n
                   for a, b in itertools.combinations(nums[i-25:i], 2)):
                continue
            return calc(i, n, nums)


def calc(i, n, nums):
    for j in range(i):
        for k in range(j):
            part = nums[k:j+1]
            if sum(part) == n:
                return min(part) + max(part)



if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
