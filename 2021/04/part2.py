#!/usr/bin/env python3

import re


def mark_number(num, board):
    return re.sub(f'(^{num} )|( {num} )|( {num}$)', ' x ', board, flags=re.MULTILINE)


def to_int_or_zero(s):
    try:
        return int(s)
    except ValueError:
        return 0


def check_board(b):
    b = [line.split() for line in b.splitlines()]
    won = all(b[i][i] == 'x' for i in range(5)) or all(b[i][4-i] == 'x' for i in range(5))
    if not won:
        for i in range(5):
            won = all(b[i][j] == 'x' for j in range(5))
            if not won:
                won = all(b[j][i] == 'x' for j in range(5))
            if won:
                break
    if won:
        return sum(sum(map(to_int_or_zero, line)) for line in b)
    return 0


def process_content(content: str):
    nums, *boards = content.split('\n\n')
    result = 0
    for num in nums.split(','):
        boards = [mark_number(num, b) for b in boards]
        newboards = []
        for b in boards:
            score = check_board(b)
            if score > 0:
                result = score * int(num)
            else:
                newboards.append(b)
        boards = newboards
    return result


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
