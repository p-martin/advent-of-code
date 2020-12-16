#!/usr/bin/env python3


def process_content(content: str):
    fielddefs, yt, nbts = content.split('\n\n')
    fields = {}
    for f in fielddefs.splitlines():
        k, v = f.split(': ')
        fields[k] = [list(map(int, r.split('-')))
                     for r in v.split(' or ')]
    errors = 0
    for nbt in nbts.splitlines()[1:]:
        for v in list(map(int, nbt.split(','))):
            if not any(any(g <= v <= G for g, G in vv)
                       for vv in fields.values()):
                errors += v
    return errors


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
