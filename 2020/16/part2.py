#!/usr/bin/env python3


def process_content(content: str):
    fielddefs, yt, nbts = content.split('\n\n')
    fields = {}
    for f in fielddefs.splitlines():
        k, v = f.split(': ')
        fields[k] = [list(map(int, r.split('-')))
                     for r in v.split(' or ')]
    validnbts = []
    for nbt in nbts.splitlines()[1:]:
        vals = list(map(int, nbt.split(',')))
        if all(any(any(g <= v <= G for g, G in vv)
                   for vv in fields.values())
               for v in vals):
            validnbts.append(vals)
    namecols = {}
    cols = list(range(len(fields)))
    for k, vv in fields.items():
        for i in list(cols):
            if all(any(g <= vals[i] <= G
                       for g, G in vv)
                   for vals in validnbts):
                namecols[k] = namecols.get(k, []) + [i]
    colnames = {}
    takencols = set()
    for name, cols in sorted(namecols.items(), key=lambda item: len(item[1])):
        col = set(cols).difference(takencols).pop()
        colnames[name] = col
        takencols.add(col)
    ytv = list(map(int, yt.splitlines()[1].split(',')))
    r = 1
    for name, i in colnames.items():
        if name.startswith('departure'):
            r *= ytv[i]
    return r


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
