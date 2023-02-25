# https://www.acmicpc.net/problem/10799

s = input()
ls = len(s)
temp = [0] * ls
for i in range(ls - 1):
    if s[i] == "(" and s[i + 1] == ")":
        temp[i] = -1
        temp[i + 1] = -1

cnt = 0
for i, x in enumerate(temp):
    if x == -1:
        cnt += 1
        continue
    temp[i] = cnt // 2

pair = dict()
stack = []
for i, char in enumerate(s):
    if temp[i] == -1:
        continue
    if char == "(":
        stack.append(i)
    else:
        if stack:
            pair[i] = stack.pop()

answer = 0
for r in pair:
    l = pair[r]
    frag = temp[r] - temp[l] + 1
    answer += frag

print(answer)
