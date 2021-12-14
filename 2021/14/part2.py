#!/usr/bin/env python3


def process_content(content: str):
    poly, rules = content.split('\n\n')

    d = {}
    for part in zip(poly[:-1], poly[1:]):
        k = ''.join(part)
        d[k] = d.get(k, 0) + 1

    rules = {k: v
             for k, v in [rule.split(' -> ')
                          for rule in rules.splitlines()]}

    for i in range(40):
        newd = {}
        for k, v in d.items():
            newchar = rules[k]
            k1 = k[0] + newchar
            k2 = newchar + k[1]
            newd[k1] = newd.get(k1, 0) + v
            newd[k2] = newd.get(k2, 0) + v
        d = newd

    chars = {}
    for k, v in d.items():
        chars[k[0]] = chars.get(k[0], 0) + v
        chars[k[1]] = chars.get(k[1], 0) + v
    chars = {k: (v//2+1 if k in (poly[0], poly[-1]) else v//2)
             for k, v in chars.items()}

    return max(chars.values()) - min(chars.values())


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
