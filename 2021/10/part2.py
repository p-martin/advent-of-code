#!/usr/bin/env python3

from statistics import median



def get_completion_score(s):
    braces = []
    for c in s:
        if c in '{([<':
            braces.append(c)
        elif braces and braces[-1] == {')':'(', ']':'[', '}':'{', '>':'<'}[c]:
            braces.pop()
        else:
            return 0
    score = 0
    for c in reversed(braces):
        score = 5 * score + {'(': 1, '[': 2, '{': 3, '<': 4}[c]
    return score



def process_content(content: str):
    scores = [get_completion_score(line)
              for line in content.splitlines()]
    return median(score
                  for score in scores
                  if score > 0)


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
