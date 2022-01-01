#!/usr/bin/env python3


def calc_forward(z, d, A, B, C):
    x = int((z%26 + B) != d)
    return (z // A) * (25*x + 1) + (d + C)*x


def calc_backward(z_target, d, A, B, C):
    x = int(A != 26)
    z = (z_target - (d + C)*x) // (25*x + 1)
    if x == 0:
        z = A*z + d - B
    if calc_forward(z, d, A, B, C) == z_target:
        return z


def solve(coeff_list, pos, z_target=0):
    for d in range(1, 10):
        new_z_target = calc_backward(z_target, d, *coeff_list[pos])
        if new_z_target is not None:
            if pos == 0:
                return str(d)
            next_d = solve(coeff_list, pos - 1, new_z_target)
            if next_d:
                return next_d + str(d)
    return ''


def process_content(content: str):
    coeff_list = [(int(dblock.splitlines()[3].split()[-1]),
                   int(dblock.splitlines()[4].split()[-1]),
                   int(dblock.splitlines()[14].split()[-1]))
                  for dblock in content.split('inp w\n')[1:]]
    return int(solve(coeff_list, len(coeff_list) - 1))


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
