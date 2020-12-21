#!/usr/bin/env python3


def process_content(content: str):
    allergenes = {}
    relations = [(ingr.split(), allerg.rstrip(')').split(', '))
                 for ingr, allerg in [line.split(' (contains ')
                                      for line in content.splitlines()]]
    for ingr, allerg in relations:
        for a in allerg:
            allergenes[a] = (allergenes[a].intersection(ingr)
                             if a in allergenes
                             else set(ingr))
    while any(len(v) > 1 for v in allergenes.values()):
        for k, v in allergenes.items():
            if len(v) == 1:
                for k2, v2 in allergenes.items():
                    if k2 != k:
                        allergenes[k2] = [x for x in v2 if x not in v]
    return ','.join(v[0] for k, v in sorted(allergenes.items()))


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
