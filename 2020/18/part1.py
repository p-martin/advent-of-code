#!/usr/bin/env python3


def process_content(content: str):
    return sum(calc(line)
               for line in content.splitlines())


def calc(line, val=0, op='+'):
    r = val
    while line:
        fc = line[0]
        if fc == '(':
            pdepth = 0
            for i, c in enumerate(line):
                pdepth += {'(': 1, ')': -1}.get(c, 0)
                if pdepth == 0:
                    rhs = calc(line[1:i])
                    r = (r + rhs) if op == '+' else (r * rhs)
                    line = line[i+1:].lstrip()
                    break
        elif fc in ('+', '*'):
            op = fc
            line = line[1:].lstrip()
        else:  # number
            n = line.split(None, 1)[0]
            line = line[len(n):].lstrip()
            n = int(n)
            r = (r + n) if op == '+' else (r * n)
    return r


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
