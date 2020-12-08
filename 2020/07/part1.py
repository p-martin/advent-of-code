#!/usr/bin/env python3

import re


def process_content(content: str):
    d = {}
    for line in content.splitlines():
        k, v = line.split(' contain ')
        d[k.rsplit(None, 1)[0]] = [re.sub(r'^[0-9]+\s+', '', vv.rsplit(None, 1)[0])
                                   for vv in v.split(', ')]
    search = {'shiny gold'}
    cont = True
    while cont:
        cont = False
        for sstr in list(search):
            for k, v in d.items():
                if sstr in v:
                    if k not in search:
                        search.add(k)
                        cont = True
    return len(search) - 1


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
