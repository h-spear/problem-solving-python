# https://www.acmicpc.net/problem/11655

hash_small = {alphabet: i for i, alphabet in enumerate("abcdefghijklmnopqrstuvwxyz")}
hash = {alphabet: i for i, alphabet in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}

string = input()
for char in string:
    if char in hash:
        print(chr(ord("A") + (hash[char] + 13) % 26), end="")
    elif char in hash_small:
        print(chr(ord("a") + (hash_small[char] + 13) % 26), end="")
    else:
        print(char, end="")
