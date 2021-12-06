#!/usr/bin/env python3


def process_content(content: str):
    nums = list(map(int, content.split(',')))
    for day in range(80):
        nums = [n-1 for n in nums]
        for i, n in list(enumerate(nums)):
            if n < 0:
                nums.append(8)
                nums[i] = 6
    return len(nums)


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
