#!/usr/bin/env python3


def process_content(content: str):
    hmap = [tuple(map(int, line))
            for line in content.splitlines()]
    lp = set()
    seen = set()
    for sy, line in enumerate(hmap):
        for sx, h in enumerate(line):
            if (sx, sy) not in seen:
                x, y = sx, sy
                while True:
                    if x > 0 and hmap[y][x-1] < h:
                        x -= 1
                    elif x < len(line)-1 and hmap[y][x+1] < h:
                        x += 1
                    elif y > 0 and hmap[y-1][x] < h:
                        y -= 1
                    elif y < len(hmap)-1 and hmap[y+1][x] < h:
                        y += 1
                    else:
                        break
                    h = hmap[y][x]
                    seen.add((x, y))
                if h < 9:
                    lp.add((x, y))
    return sum(hmap[y][x] + 1 for x, y in lp)


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
