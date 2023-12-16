#!/usr/bin/env python3


def process_content(content: str):
    blocks = content.strip().split("\n\n")
    seeds = list(map(int, blocks[0].split(":")[1].split()))

    for b in blocks:
        map_, offs = [], []
        coeffs = [tuple(map(int, line.split())) for line in b.splitlines()[1:]]
        for dst, src, length in sorted(coeffs, key=lambda row: row[1]):
            map_ += [src, src+length]
            offs += [dst-src, 0]

        newseeds = []
        for seed in seeds:
            for i in range(len(map_) - 1):
                if map_[i] <= seed < map_[i+1]:
                    newseeds.append(seed + offs[i])
                    break
            else:
                newseeds.append(seed)
        seeds = newseeds

    return min(seeds)


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
