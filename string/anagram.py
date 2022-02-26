# https://www.acmicpc.net/problem/6996

from collections import Counter

for tc in range(int(input())):
    a, b = input().split()
    print("{} & {} are".format(a, b), end=" ")
    if Counter(a) != Counter(b):
        print("NOT", end=" ")
    print("anagrams.")
