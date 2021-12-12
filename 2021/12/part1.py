#!/usr/bin/env python3


def process_content(content: str):
    graph = {}
    for line in content.splitlines():
        a, b = line.split('-')
        graph[a] = graph.get(a, set()) | {b}
        graph[b] = graph.get(b, set()) | {a}

    paths = [['start']]
    changed = True
    while changed:
        changed = False
        newpaths = []
        for p in paths:
            a = p[-1]
            if a == 'end':
                newpaths.append(p)
            else:
                for b in graph[a]:
                    if b.lower() != b or b not in p:
                        newpaths.append(p + [b])
                        changed = True
        paths = newpaths

    return len(paths)


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
