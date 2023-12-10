#!/usr/bin/env python3

import re


NUMS = "one two three four five six seven eight nine".split()


def process_content(content: str):
    res = 0
    nd = {num: n for n, num in enumerate(NUMS, 1)}

    for line in content.strip().splitlines():
        m = re.search("("+"|".join(NUMS)+")", line)
        a = int(re.search(r"(\d)",
                          line.replace(m.group(1),
                                       str(nd[m.group(1)]),
                                       1) if m else line
                          ).group(1))
        m = re.search("("+"|".join(num[::-1] for num in NUMS)+")", line[::-1])
        b = int(re.search(r"(\d)",
                          line[::-1].replace(m.group(1),
                                             str(nd[m.group(1)[::-1]]),
                                             1) if m else line[::-1]
                          ).group(1))
        res += a*10 + b

    return res


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
