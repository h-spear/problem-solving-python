# https://www.acmicpc.net/problem/20114

n, h, w = map(int, input().split())

string = []
for _ in range(h):
    string.append(input())

temp = ["?"] * (n * w)

for j in range(n * w):
    for i in range(h):
        if string[i][j] != "?":
            temp[j] = string[i][j]

for j in range(0, n * w, w):
    s = set(temp[j : j + w]) - set("?")
    if s:
        print(s.pop(), end="")
    else:
        print("?", end="")
