#!/usr/bin/env python3


def process_content(content: str):
    timers = {}
    for t in map(int, content.split(',')):
        timers[t] = timers.get(t, 0) + 1

    for day in range(256):
        newtimers = {}
        for t, cnt in timers.items():
            t -= 1
            if t < 0:
                newtimers[8] = newtimers.get(8, 0) + cnt
                t = 6
            newtimers[t] = newtimers.get(t, 0) + cnt
        timers = newtimers

    return sum(timers.values())


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
