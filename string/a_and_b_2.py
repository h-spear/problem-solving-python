# https://www.acmicpc.net/problem/12919


def dfs(t):
    global flag
    if len(t) == ls:
        flag = t == s
        return

    if not flag and t[-1] == "A":
        dfs(list(t[:-1]))

    if not flag and t[0] == "B":
        dfs(list(reversed(t[1:])))


s = list(input())
t = list(input())
ls = len(s)
flag = False

dfs(t)

if flag:
    print(1)
else:
    print(0)
