#!/usr/bin/env python3


def process_content(content: str):
    lines = content.splitlines()
    for i in range(len(lines)):
        line = lines[i]
        if line.startswith('jmp'):
            line = line.replace('jmp', 'nop')
        elif line.startswith('nop'):
            line = line.replace('nop', 'jmp')
        else:
            continue
        r = check(lines[:i] + [line] + lines[i+1:])
        if r is not None:
            return r


def check(lines):
    ip, acc = 0, 0
    visited = set()
    while True:
        if ip in visited:
            return None
        elif ip >= len(lines):
            break
        visited.add(ip)
        cmd, val = lines[ip].split()
        if cmd == 'nop':
            ip += 1
        elif cmd == 'acc':
            acc += int(val)
            ip += 1
        elif cmd == 'jmp':
            ip += int(val)
    return acc


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
