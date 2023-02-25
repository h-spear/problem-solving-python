# https://www.acmicpc.net/problem/1213

from collections import Counter


def fn(string):
    counter = Counter(string)
    odd_cnt = 0
    odd_char = ""
    evens = []
    for char, i in counter.items():
        if i & 1 == 1:
            odd_cnt += 1
            odd_char = char
            evens.extend([char] * (i // 2))
            if odd_cnt == 2:
                print("I'm Sorry Hansoo")
                return
        else:
            evens.extend([char] * (i // 2))

    evens.sort()
    prefix = "".join(evens)
    print(prefix, odd_char, prefix[::-1], sep="")


string = input()
fn(string)
