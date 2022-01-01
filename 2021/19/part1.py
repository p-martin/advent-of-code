#!/usr/bin/env python3


ROTATIONS = [(xa, ya, (xa[1]*ya[2]-xa[2]*ya[1], xa[2]*ya[0]-xa[0]*ya[2], xa[0]*ya[1]-xa[1]*ya[0]))
             for xa in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
             for ya in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
             if xa[0]*ya[0] + xa[1]*ya[1] + xa[2]*ya[2] == 0]


def check_overlapping(ref, new):
    for r in ROTATIONS:
        newrot = {(r[0][0]*x+r[0][1]*y+r[0][2]*z,
                   r[1][0]*x+r[1][1]*y+r[1][2]*z,
                   r[2][0]*x+r[2][1]*y+r[2][2]*z)
                  for x, y, z in new}
        for rpx, rpy, rpz in ref:
            for npx, npy, npz in newrot:
                dx, dy, dz = rpx-npx, rpy-npy, rpz-npz
                newtl = {(x+dx, y+dy, z+dz)
                         for x, y, z in newrot}
                if len(ref.intersection(newtl)) >= 12:
                    return newtl
    return None


def process_content(content: str):
    blocks = {int(block.splitlines()[0].split()[-2]): {tuple(map(int, beacon.split(',')))
                                                           for beacon in block.splitlines()[1:]}
              for block in content.strip().split('\n\n')}

    all_beacons = blocks[0]
    lastknowns, unknowns = {0}, set(range(1, len(blocks)))

    while unknowns:
        newunknowns, newlastknowns = set(), set()
        for u in unknowns:
            found = False
            for lk in lastknowns:
                if newtl := check_overlapping(blocks[lk], blocks[u]):
                    all_beacons |= newtl
                    blocks[u] = newtl
                    newlastknowns.add(u)
                    found = True
                    break
            if not found:
                newunknowns.add(u)
        lastknowns, unknowns = newlastknowns, newunknowns

    return len(all_beacons)


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
