#!/usr/bin/env python3


def process_content(content: str):
    inss, graph = content.strip().split("\n\n")
    graph = {src: tuple(dst.strip("()").split(", "))
             for src, dst in map(lambda line: line.split(" = "), graph.splitlines())}

    node, i = "AAA", 0
    while node != "ZZZ":
        node = graph[node][inss[i % len(inss)] == "R"]
        i += 1

    return i


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
