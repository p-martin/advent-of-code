#!/usr/bin/env python3

from math import prod
from operator import gt, lt, eq


def get_packet_val(b, maxpackets=None, outermost=False):
    origlen = len(b)
    vl = []
    p = 1
    while (((not outermost and b) or
            (outermost and not b.startswith('000'))) and
            (maxpackets is None or p <= maxpackets)):
        version, b = int(b[:3], 2), b[3:]
        type_id, b = int(b[:3], 2), b[3:]
        if type_id == 4:
            val = 0
            while b.startswith('1'):
                val = (val << 4) + int(b[1:5], 2)
                b = b[5:]
            val = (val << 4) + int(b[1:5], 2)
            b = b[5:]  # last group
        else:
            length_type, b = int(b[:1], 2), b[1:]
            if length_type == 0:
                opval, b = int(b[:15], 2), b[15:]
                newvl = get_packet_val(b[:opval])[0]
                b = b[opval:]
            else:
                opval, b = int(b[:11], 2), b[11:]
                newvl, consumed = get_packet_val(b, maxpackets=opval)
                b = b[consumed:]
            func = {0: sum, 1: prod, 2: min, 3: max, 5: gt, 6: lt, 7: eq}[type_id]
            val = func(*newvl) if type_id >= 5 else func(newvl)
        vl.append(val)
        p += 1
    return vl, origlen - len(b)


def process_content(content: str):
    b = ''.join(bin(int(c, 16))[2:].zfill(4)
                for c in content.strip())
    vl, __ = get_packet_val(b, outermost=True)
    return vl[0]


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
