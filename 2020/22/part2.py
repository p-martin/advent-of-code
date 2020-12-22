#!/usr/bin/env python3


def process_content(content: str):
    deck1, deck2 = [list(map(int, block.splitlines()[1:]))
                    for block in content.strip().split('\n\n')]
    return recursivecombat(deck1, deck2)[1]


def recursivecombat(deck1, deck2):
    occurred = set()
    while deck1 and deck2:
        if (tuple(deck1), tuple(deck2)) in occurred:
            return 1, sum(i * c for i, c in enumerate(reversed(deck1), 1))
        occurred.add((tuple(deck1), tuple(deck2)))
        if deck1[0] <= len(deck1) - 1 and deck2[0] <= len(deck2) - 1:
            if 1 == recursivecombat([x for x in deck1[1:deck1[0]+1]],
                                    [x for x in deck2[1:deck2[0]+1]],)[0]:
                deck1, deck2 = deck1[1:] + [deck1[0], deck2[0]], deck2[1:]
            else:
                deck1, deck2 = deck1[1:], deck2[1:] + [deck2[0], deck1[0]]
        elif deck1[0] > deck2[0]:
            deck1, deck2 = deck1[1:] + [deck1[0], deck2[0]], deck2[1:]
        else:
            deck1, deck2 = deck1[1:], deck2[1:] + [deck2[0], deck1[0]]
    return ((1, sum(i * c for i, c in enumerate(reversed(deck1), 1)))
            if deck1
            else (2, sum(i * c for i, c in enumerate(reversed(deck2), 1))))


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
