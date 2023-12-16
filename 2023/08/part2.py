#!/usr/bin/env python3

import math


def process_content(content: str):
    inss, graph = content.strip().split("\n\n")
    graph = {src: tuple(dst.strip("()").split(", "))
             for src, dst in map(lambda line: line.split(" = "), graph.splitlines())}

    vals = []
    for node in graph.keys():
        if node.endswith("A"):
            i = 0
            while not node.endswith("Z") or i % len(inss) != 0:
                node = graph[node][inss[i % len(inss)] == "R"]
                i += 1
            vals.append(i)

    return math.lcm(*vals)


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
