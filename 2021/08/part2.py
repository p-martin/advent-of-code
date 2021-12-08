#!/usr/bin/env python3


def determine_configs(configs):
    result = {}
    n14 = {}

    for conf in configs.split():
        conf = ''.join(sorted(conf))
        if len(conf) == 2:
            result[conf] = 1
            n14[1] = conf
        elif len(conf) == 4:
            result[conf] = 4
            n14[4] = conf
        elif len(conf) == 3:
            result[conf] = 7
        elif len(conf) == 7:
            result[conf] = 8

    for conf in configs.split():
        conf = ''.join(sorted(conf))
        confset = set(conf)
        if len(conf) == 6:
            if len(confset.intersection(n14[4])) == 4:
                result[conf] = 9
            elif len(confset.intersection(n14[1])) == 1:
                result[conf] = 6
            else:
                result[conf] = 0
        elif len(conf) == 5:
            if len(confset.intersection(n14[1])) == 2:
                result[conf] = 3
            elif len(confset.intersection(n14[4])) == 3:
                result[conf] = 5
            else:
                result[conf] = 2

    return result


def process_content(content: str):
    result = 0
    for line in content.splitlines():
        configs, outp = line.split(' | ')
        confdict = determine_configs(configs)

        val = 0
        for s in outp.split():
            val = val*10 + confdict[''.join(sorted(s))]
        result += val

    return result


if __name__ == '__main__':
    import os
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file, encoding='utf-8') as f:
        result = process_content(f.read())
    print(f'result = {repr(result)}')
