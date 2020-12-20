#!/usr/bin/env python3

import re


def process_content(content: str):
    ruledefs, msgs = content.split('\n\n')
    rules = {}
    for r in ruledefs.splitlines():
        i, r = r.split(': ')
        i = int(i)
        if r.startswith('"'):
            rules[i] = r.strip(' "')
        elif '|' in r:
            rules[i] = tuple(list(map(int, p.split()))
                             for p in r.split(' | '))
        else:
            rules[i] = list(map(int, r.split()))
    rule0 = make_regex(rules[0], rules)
    return sum(1 for msg in msgs.splitlines()
               if re.fullmatch(rule0, msg))


def make_regex(term, rules):
    if isinstance(term, str):
        return term
    if isinstance(term, int):
        return make_regex(rules[term], rules)
    if isinstance(term, list):
        return '(%s)' % ''.join(make_regex(x, rules) for x in term)
    return '(%s)' % '|'.join(make_regex(x, rules) for x in term)


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
