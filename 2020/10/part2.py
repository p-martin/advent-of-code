#!/usr/bin/env python3


def process_content(content: str):
    groups = []
    cg = [0]
    for n in sorted(map(int, content.splitlines())):
        if n - cg[-1] > 1:
            groups.append(cg)
            cg = [n]
        else:
            cg.append(n)
    groups.append(cg)
    w = 1
    for g in groups:
        w *= calc(len(g))
    return w


def calc(gl):
    if gl < 3:
        return 1
    elif gl == 3:
        return 2
    return calc(gl-1) + calc(gl-2) + calc(gl-3)


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
