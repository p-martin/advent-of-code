#!/usr/bin/env python3


def process_content(content: str):
    blocks = content.strip().split("\n\n")
    seeds = list(map(int, blocks[0].split(":")[1].split()))
    starts, lengths = seeds[::2], seeds[1::2]
    ends = [s+l for s, l in zip(starts, lengths)]

    for b in blocks:
        map_, offs = [], []
        coeffs = [tuple(map(int, line.split())) for line in b.splitlines()[1:]]
        for dst, src, length in sorted(coeffs, key=lambda row: row[1]):
            map_ += [src, src+length]
            offs += [dst-src, 0]

        newstarts, newends = [], []
        for start, end in zip(starts, ends):
            for i in range(len(map_) - 1):
                if map_[i] <= start < map_[i+1]:
                    newstarts.append(start + offs[i])
                    if map_[i] <= end < map_[i+1]:
                        newends.append(end + offs[i])
                        break
                    else:
                        newends.append(map_[i+1] + offs[i])
                        start = map_[i+1]
            else:
                newstarts.append(start)
                newends.append(end)
        starts, ends = newstarts, newends

    return min(starts)


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
