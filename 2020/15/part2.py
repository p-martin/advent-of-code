#!/usr/bin/env python3


def process_content(content: str):
    nums = list(map(int, content.splitlines()[0].split(',')))
    lastIndexes = {n: i for i, n in enumerate(nums[:-1])}
    cn = nums[-1]
    ln = cn
    for i in range(len(nums), 30000000):
        try:
            li = lastIndexes[cn]
            cn = i - 1 - li
        except KeyError:
            cn = 0
        lastIndexes[ln] = i - 1
        ln = cn
    return cn


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
