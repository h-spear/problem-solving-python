# https://www.acmicpc.net/problem/1622

from collections import Counter

while 1:
    try:
        a = input()
        b = input()
        counter = Counter(a) & Counter(b)
        characters = []
        for char, i in counter.items():
            characters.extend([char] * i)
        characters.sort()
        print("".join(characters))
    except:
        break
