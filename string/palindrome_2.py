# https://www.acmicpc.net/problem/8892

from itertools import combinations


def is_palindrome(string):
    ls = len(string)
    for i in range(ls // 2):
        if string[i] != string[ls - i - 1]:
            return False
    return True


def solve():
    k = int(input())
    words = []
    for _ in range(k):
        words.append(input())

    for a, b in combinations(words, 2):
        str = a + b
        if is_palindrome(str):
            print(str)
            return

        str = b + a
        if is_palindrome(str):
            print(str)
            return

    print(0)


for tc in range(int(input())):
    solve()
