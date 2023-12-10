#!/usr/bin/env python3


def process_content(content: str):
    res = []
    for line in content.splitlines():
        a, b = line.split(": ")[1].split(" | ")
        wc = len(set(map(int, a.split())).intersection(map(int, b.split())))
        res.append([wc, 1])
    for i, (wc, n) in enumerate(res[:]):
        for ii in range(1, wc+1):
            res[i+ii][1] += n
    return sum(r[1] for r in res)


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
