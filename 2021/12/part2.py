#!/usr/bin/env python3


def process_content(content: str):
    graph = {}
    for line in content.splitlines():
        a, b = line.split('-')
        if a != 'end' and b != 'start':
            graph[a] = graph.get(a, set()) | {b}
        if b != 'end' and a != 'start':
            graph[b] = graph.get(b, set()) | {a}

    paths = [['start']]
    twice = [False]
    changed = True
    while changed:
        changed, newpaths, newtwice = False, [], []
        for p, tw in zip(paths, twice):
            a = p[-1]
            if a == 'end':
                newpaths.append(p)
                newtwice.append(tw)
            else:
                for b in graph[a]:
                    tw_needed = b.lower() == b and b in p
                    if not tw_needed or not tw:
                        newpaths.append(p + [b])
                        newtwice.append(tw or tw_needed)
                        changed = True
        paths, twice = newpaths, newtwice

    return len(paths)


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
