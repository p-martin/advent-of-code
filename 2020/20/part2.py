#!/usr/bin/env python3

import re


def process_content(content: str):
    tiles = {}
    for td in content.strip().split('\n\n'):
        title, *rest = td.splitlines()
        tid = int(title.strip('Tile :'))
        tiles[tid] = rest
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
        if not possl and not posst:
            firstcorner = tid1
            firstcornertile = tile1
            break
        if not possr and not posst:
            firstcorner = tid1
            firstcornertile = fliph(tile1)
            break
        if not possl and not possb:
            firstcorner = tid1
            firstcornertile = flipv(tile1)
            break
        if not possr and not possb:
            firstcorner = tid1
            firstcornertile = fliph(flipv(tile1))
            break

    field = {0: {0: firstcornertile}}
    chosen = {firstcorner}
    x = y = 0
    while True:
        if y == 0:
            __, l2, __, __ = getborders(field[y][x])
            found = False
            for ntid, nt in tiles.items():
                if ntid in chosen:
                    continue
                t, r, b, l = getborders(nt)
                tnt = None
                if l2 == l:
                    tnt = nt
                elif l2 == r:
                    tnt = fliph(nt)
                elif l2 == t[::-1]:
                    tnt = rotate(nt)
                elif l2 == b:
                    tnt = rotate(flipv(fliph(nt)))
                elif l2 == l[::-1]:
                    tnt = flipv(nt)
                elif l2 == r[::-1]:
                    tnt = flipv(fliph(nt))
                elif l2 == t:
                    tnt = flipv(rotate(nt))
                elif l2 == b[::-1]:
                    tnt = flipv(rotate(flipv(fliph(nt))))
                if tnt:
                    found = True
                    x += 1
                    field[y][x] = tnt
                    chosen.add(ntid)
                    break
            if not found:
                linelength = len(chosen)
                y += 1
                x = -1
        else:
            x += 1
            if x >= linelength:
                y += 1
                x = 0
            __, __, t2, __ = getborders(field[y-1][x])
            found = False
            for ntid, nt in tiles.items():
                if ntid in chosen:
                    continue
                t, r, b, l = getborders(nt)
                tnt = None
                if t2 == t:
                    tnt = nt
                elif t2 == b:
                    tnt = flipv(nt)
                elif t2 == t[::-1]:
                    tnt = fliph(nt)
                elif t2 == b[::-1]:
                    tnt = fliph(flipv(nt))
                elif t2 == l:
                    tnt = fliph(rotate(rotate(rotate(nt))))
                elif t2 == l[::-1]:
                    tnt = rotate(rotate(rotate(nt)))
                elif t2 == r:
                    tnt = rotate(nt)
                elif t2 == r[::-1]:
                    tnt = fliph(rotate(nt))
                if tnt:
                    found = True
                    if y not in field:
                        field[y] = {}
                    field[y][x] = tnt
                    chosen.add(ntid)
                    break
            if not found:
                break
        if y * x >= len(tiles):
            break
    tilesize = len(firstcornertile)
    fullimage = []
    for y in range(len(field)):
        for i in range(1, tilesize-1):
            fullimage.append(''.join(field[y][x][i][1:-1]
                                     for x in range(len(field[y]))))
    sm = ['                  # ',
          '#    ##    ##    ###',
          ' #  #  #  #  #  #   ']
    smheight, smwidth = len(sm), len(sm[0])
    sm = '\n'.join(sm)
    smfields = sm.count('#')
    sm = sm.replace(' ', '[.#]')
    foundlist = []
    for i in range(8):
        if i in (1, 2, 3, 5, 6, 7):
            fullimage = rotate(fullimage)
        elif i == 4:
            fullimage = fliph(rotate(fullimage))
        for x in range(len(fullimage[0]) + 1 - smwidth):
            for y in range(len(fullimage) + 1 - smheight):
                checkarea = '\n'.join(line[x:x+smwidth] for line in fullimage[y:y+smheight])
                if re.fullmatch(sm, checkarea):
                    foundlist.append((x, y))
    return ''.join(fullimage).count('#') - len(foundlist) * smfields


def getborders(tile):
    top = tile[0]
    bottom = tile[-1]
    left = ''.join(line[0] for line in tile)
    right = ''.join(line[-1] for line in tile)
    return top, right, bottom, left


def fliph(tile):
    return [line[::-1] for line in tile]


def flipv(tile):
    return tile[::-1]


def rotate(tile):
    # rotate 90° counterclockwise
    return [''.join(line[-1-i] for line in tile)
            for i in range(len(tile))]


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
