#!/usr/bin/env python3

import sys
import math


COSTS = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}


def is_final_state(state, maxy):
    return all(state.get((x, y)) == c
               for y in range(2, maxy+1)
               for x, c in zip(range(3, 10, 2), 'ABCD'))


def serialize_state(state):
    return


def solve(init_state):
    maxy = max(y for x, y in init_state.keys())
    mincost = 0
    states = {0: [init_state]}
    mincost_for_state = {serialize_state(init_state): 0}

    def move():
        newstate = {k: v
                    for k, v in state.items()
                    if k != (x, y)} | {(tx, ty): c}
        newcost = mincost + (abs(ty-y) + abs(tx-x)) * COSTS[c]
        key = tuple(sorted(newstate.items()))
        if key not in mincost_for_state or mincost_for_state[key] > newcost:
            states.setdefault(newcost, []).append(newstate)
            mincost_for_state[key] = newcost

    while states:
        while mincost not in states:
            mincost += 1
        minstates = states[mincost]
        state = minstates.pop(0)
        if is_final_state(state, maxy):
            return mincost
        if not minstates:
            del states[mincost]
        for (x, y), c in state.items():
            if y >= 2:  # from room to hallway
                if y > 2 and (x, y-1) in state:
                    continue  # blocked
                if all(state[(x, yy)] == 'ABCD'[(x-3)//2]
                       for yy in range(y, maxy+1)):
                    continue  # final place reached
                ty = 1
                for tx in range(x-1, 0, -1):
                    if tx not in (3, 5, 7, 9):
                        if (tx, ty) in state:
                            break  # hallway blocked
                        move()
                for tx in range(x+1, 12):
                    if tx not in (3, 5, 7, 9):
                        if (tx, ty) in state:
                            break  # hallway blocked
                        move()
            else:  # from hallway to target room
                tx = (ord(c)-65)*2 + 3
                offs = -1 if tx < x else 1
                ok = True
                for xx in range(x + offs, tx + offs, offs):
                    if (xx, 1) in state:
                        ok = False  # blocked
                        break
                if ok:
                    ty = maxy
                    while (tx, ty) in state:
                        if state[(tx, ty)] != c:
                            ok = False  # target room not yet cleared
                            break
                        ty -= 1
                    if ok:
                        move()
    assert False, 'no solution found'


def process_content(content: str):
    state = {(x, y): c
             for y, line in enumerate(content.splitlines())
             for x, c in enumerate(line)
             if c in 'ABCD'}
    result = solve(state)
    return result


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
