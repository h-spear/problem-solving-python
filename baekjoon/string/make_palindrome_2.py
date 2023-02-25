# https://www.acmicpc.net/problem/1254

s = input()
rev_s = s[::-1]
ls = len(s)

for i in range(ls):
    if s[i:] == rev_s[: ls - i]:
        print(ls + i)
        break
