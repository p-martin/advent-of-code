#!/usr/bin/env python3


def process_content(content: str):
    passports = content.split('\n\n')
    return len([pp
                for pp in passports
                if all(key+':' in pp for key in 'byr iyr eyr hgt hcl ecl pid'.split())])


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
