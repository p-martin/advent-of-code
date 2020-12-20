#!/usr/bin/env python3

import re


def process_content(content: str):
    ruledefs, msgs = content.split('\n\n')
    rules = {}
    for r in ruledefs.splitlines():
        i, r = r.split(': ')
        i = int(i)
        r = {8: '42 | 42 8', 11: '42 31 | 42 11 31'}.get(i, r)
        if r.startswith('"'):
            rules[i] = r.strip(' "')
        elif '|' in r:
            rules[i] = tuple(list(map(int, p.split()))
                             for p in r.split(' | '))
        else:
            rules[i] = list(map(int, r.split()))
    msgs = msgs.splitlines()
    maxdepth = max(len(msg) for msg in msgs)
    rule0 = make_regex(rules[0], rules, 0, maxdepth)
    return sum(1 for msg in msgs
               if re.fullmatch(rule0, msg))


def make_regex(term, rules, depth, maxdepth):
    if depth >= maxdepth:
        return ''
    if isinstance(term, str):
        return term
    if isinstance(term, int):
        return make_regex(rules[term], rules, depth+1, maxdepth)
    if isinstance(term, list):
        return '(%s)' % ''.join(make_regex(x, rules, depth+1, maxdepth) for x in term)
    return '(%s)' % '|'.join(make_regex(x, rules, depth+1, maxdepth) for x in term)


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
