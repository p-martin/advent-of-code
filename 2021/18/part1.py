#!/usr/bin/env python3

from json import loads


def snail_add(v1, v2):
    return ['['] + v1 + [','] + v2 + [']']


def snail_explode(v):
    changed = True
    while changed:
        changed = False
        depth = 0
        for i, c in enumerate(v):
            if c == '[':
                depth += 1
            elif c == ']':
                depth -= 1
            elif (isinstance(c, int) and depth > 4 and
                    '[' not in v[i:i+3] and ']' not in v[i:i+3]):
                r = None
                for j in range(i+5, len(v)):
                    if isinstance(v[j], int):
                        r = j, v[j] + v[i+2]
                        break
                if r:
                    v = v[:r[0]] + [r[1]] + v[r[0] + 1:]
                l = None
                for j in range(i-1, 0, -1):
                    if isinstance(v[j], int):
                        l = j, v[j] + v[i]
                        break
                v = v[:i-1] + [0] + v[i+4:]
                if l:
                    v = v[:l[0]] + [l[1]] + v[l[0] + 1:]
                changed = True
                break
    return v


def snail_split(v):
    for i, c in enumerate(v):
        if isinstance(c, int) and c > 9:
            return v[:i] + ['[', c//2, ',', (c+1)//2, ']'] + v[i+1:]
    return v


def calc_magnitude(v):
    a = calc_magnitude(v[0]) if isinstance(v[0], list) else v[0]
    b = calc_magnitude(v[1]) if isinstance(v[1], list) else v[1]
    return a*3 + b*2


def process_content(content: str):
    vals = [[c if c in ',[]' else int(c)
             for c in line]
            for line in content.splitlines()]

    val = vals[0]
    for nval in vals[1:]:
        val = snail_add(val, nval)
        changed = True
        while changed:
            newval = snail_split(snail_explode(val))
            changed, val = newval != val, newval

    return calc_magnitude(loads(''.join(map(str, val))))


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
