#!/usr/bin/env python3


def process_content(content: str):
    nums = [int(line.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1'), 2)
            for line in content.splitlines()]
    for n in range(max(nums) + 1):
        if n-1 in nums and n not in nums and n+1 in nums:
            return n


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
