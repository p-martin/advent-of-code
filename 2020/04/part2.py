#!/usr/bin/env python3

import re


def process_content(content: str):
    passports = content.split('\n\n')
    return len([pp
                for pp in passports
                if is_valid(pp)])


def is_valid(pp):
    d = dict(kv.split(':') for kv in pp.split())
    try:
        if not 1920 <= int(d['byr']) <= 2002:
            return False
        if not 2010 <= int(d['iyr']) <= 2020:
            return False
        if not 2020 <= int(d['eyr']) <= 2030:
            return False
        if not (d['hgt'].endswith('cm') and 150 <= int(d['hgt'][:-2]) <= 193 or
                d['hgt'].endswith('in') and 59 <= int(d['hgt'][:-2]) <= 76):
            return False
        if not re.fullmatch(r'#[0-9a-f]{6}', d['hcl']):
            return False
        if d['ecl'] not in 'amb blu brn gry grn hzl oth'.split():
            return False
        if not re.fullmatch(r'[0-9]{9}', d['pid']):
            return False
        return True
    except KeyError:
        return False


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
