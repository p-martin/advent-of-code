#!/usr/bin/env python3


def process_content(content: str):
    mem = {}
    for line in content.splitlines():
        if line.startswith('mem'):
            pos, val = map(int, line.lstrip('mem[').split('] ='))
            pos = bin(pos)[2:].zfill(36)
            newpos = [cp if cm == '0' else cm
                      for cp, cm in zip(pos, mask)]
            numx = newpos.count('X')
            if numx == 0:
                mem[int(''.join(newpos), 2)] = val
            else:
                for flt in range(2 ** numx):
                    fs = bin(flt)[2:].zfill(numx)
                    ifs = 0
                    np = list(newpos)
                    for inp, c in enumerate(np):
                        if c == 'X':
                            np[inp] = fs[ifs]
                            ifs += 1
                    mem[int(''.join(np), 2)] = val
        elif line.startswith('mask'):
            mask = line.split('=')[1].strip()
    return sum(mem.values())


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
