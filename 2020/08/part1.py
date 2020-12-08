#!/usr/bin/env python3


def process_content(content: str):
    ip, acc = 0, 0
    visited = set()
    lines = content.splitlines()
    while ip not in visited:
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
