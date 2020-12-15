#!/usr/bin/env python3


def process_content(content: str):
    nums = list(map(int, content.splitlines()[0].split(',')))
    for i in range(2020 - len(nums)):
        n1, rest = nums[-1], nums[:-1]
        nums.append(list(reversed(rest)).index(n1) + 1
                    if n1 in rest
                    else 0)
    return nums[-1]


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
