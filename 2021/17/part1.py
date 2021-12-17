#!/usr/bin/env python3


def process_content(content: str):
    [(x1, x2), (y1, y2)] = [map(int, r.split('=')[-1].split('..'))
                            for r in content.strip().split(': ')[-1].split(', ')]

    result = 0
    for init_vx in range(x2 + 2):
        for init_vy in range(y1-1, -y1+2):
            vx, vy = init_vx, init_vy
            x = y = 0
            maxy = 0
            hit = False
            while x <= x2 and y >= y1:
                x, y = x + vx, y + vy
                maxy = max(maxy, y)
                if vx > 0:
                    vx -= 1
                vy -= 1
                if x1 <= x <= x2 and y1 <= y <= y2:
                    hit = True
                    break
            if hit:
                result = max(result, maxy)
    return result


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
