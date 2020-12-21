#!/usr/bin/env python3


def process_content(content: str):
    allergenes = {}
    allingr = set()
    relations = [(ingr.split(), allerg.rstrip(')').split(', '))
                 for ingr, allerg in [line.split(' (contains ')
                                      for line in content.splitlines()]]
    for ingr, allerg in relations:
        allingr = allingr.union(ingr)
        for a in allerg:
            allergenes[a] = (allergenes[a].intersection(ingr)
                             if a in allergenes
                             else set(ingr))
    for ingr in allergenes.values():
        allingr = allingr.difference(ingr)
    return sum(ingr.count(i)
               for i in allingr
               for ingr, __ in relations)


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
