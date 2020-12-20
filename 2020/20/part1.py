#!/usr/bin/env python3


def process_content(content: str):
    tiles = {}
    for td in content.strip().split('\n\n'):
        title, *rest = td.splitlines()
        tid = int(title.strip('Tile :'))
        tiles[tid] = rest
    val = 1
    for tid1, tile1 in tiles.items():
        t1, r1, b1, l1 = getborders(tile1)
        possl, possr, posst, possb = [], [], [], []
        for tid2, tile2 in tiles.items():
            if tid2 != tid1:
                t2, r2, b2, l2 = getborders(tile2)
                if l1 in (l2, r2, t2, b2, l2[::-1], r2[::-1], t2[::-1], b2[::-1]):
                    possl.append(tid2)
                if r1 in (l2, r2, t2, b2, l2[::-1], r2[::-1], t2[::-1], b2[::-1]):
                    possr.append(tid2)
                if t1 in (l2, r2, t2, b2, l2[::-1], r2[::-1], t2[::-1], b2[::-1]):
                    posst.append(tid2)
                if b1 in (l2, r2, t2, b2, l2[::-1], r2[::-1], t2[::-1], b2[::-1]):
                    possb.append(tid2)
        if bool(possl) + bool(possr) + bool(posst) + bool(possb) == 2:
            val *= tid1
    return val


def getborders(tile):
    top = tile[0]
    bottom = tile[-1]
    left = ''.join(line[0] for line in tile)
    right = ''.join(line[-1] for line in tile)
    return top, right, bottom, left


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
