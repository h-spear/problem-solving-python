# https://www.acmicpc.net/problem/19844

import re


def fn(string):
    words = string.replace("-", " ").split()
    prefix = ["c'", "j'", "n'", "m'", "t'", "s'", "l'", "d'", "qu'"]
    vowel = ["a", "e", "i", "o", "u", "h"]
    patterns = []
    for pre in prefix:
        for vo in vowel:
            patterns.append(re.compile("^{}{}".format(pre, vo)))

    answer = len(words)
    for word in words:
        if "'" not in word:
            continue
        for pattern in patterns:
            if pattern.search(word) != None:
                answer += 1
    print(answer)


string = input()
fn(string)
