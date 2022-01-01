#!/usr/bin/env python3


def process_content(content: str):
    xvals, yvals, zvals, oncubes = [], [], [], set()

    for i, line in enumerate(content.strip().splitlines()):
        onoff, coords = line.split()
        for vals, (start, end) in zip([xvals, yvals, zvals],
                                      [list(map(int, coord.split('=')[-1].split('..')))
                                       for coord in coords.split(',')]):
            vals.append((start, i, set.add))
            vals.append((end+1, i, set.remove))
        if onoff == 'on':
            oncubes.add(i)

    num_x, handled_until_x, relevant_ids_x = 0, 0, set()
    for x, id_x, add_or_remove_x in sorted(xvals):
        num_y, handled_until_y, relevant_ids_y = 0, 0, set()
        for y, id_y, add_or_remove_y in sorted(y for y in yvals
                                               if y[1] in relevant_ids_x):
            num_z, handled_until_z, relevant_ids_z = 0, 0, set()
            for z, id_z, add_or_remove_z in sorted(z for z in zvals
                                                   if z[1] in relevant_ids_y):
                if relevant_ids_z and max(relevant_ids_z) in oncubes:
                    num_z += z - handled_until_z
                add_or_remove_z(relevant_ids_z, id_z)
                handled_until_z = z
            num_y += (y - handled_until_y) * num_z
            add_or_remove_y(relevant_ids_y, id_y)
            handled_until_y = y
        num_x += (x - handled_until_x) * num_y
        add_or_remove_x(relevant_ids_x, id_x)
        handled_until_x = x

    return num_x


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
