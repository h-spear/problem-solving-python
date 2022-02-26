# https://www.acmicpc.net/problem/1718

plaintext = list(input())
key = input()

i = 0
hash = {alphabet: i for i, alphabet in enumerate("abcdefghijklmnopqrstuvwxyz")}
for char in plaintext:
    if char != " ":
        cipher = chr(ord("a") + (hash[char] - hash[key[i]] - 1) % 26)
        print(cipher, end="")
    else:
        print(" ", end="")
    i = (i + 1) % len(key)

print()
