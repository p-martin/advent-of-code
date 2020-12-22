#!/usr/bin/env python3


def process_content(content: str):
    deck1, deck2 = [list(map(int, block.splitlines()[1:]))
                    for block in content.strip().split('\n\n')]
    while deck1 and deck2:
        if deck1[0] > deck2[0]:
            deck1, deck2 = deck1[1:] + [deck1[0], deck2[0]], deck2[1:]
        else:
            deck1, deck2 = deck1[1:], deck2[1:] + [deck2[0], deck1[0]]
    return (sum(i * c for i, c in enumerate(reversed(deck1), 1)) +
            sum(i * c for i, c in enumerate(reversed(deck2), 1)))


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
