# https://www.acmicpc.net/problem/12101

n, k = map(int, input().split())
answer = ""
cnt = 0


def dfs(num, path):
    global cnt, answer
    if answer:
        return

    if num > n:
        return

    if num == n:
        cnt += 1

        if cnt == k:
            answer = path
            return

    dfs(num + 1, path + "+1")
    dfs(num + 2, path + "+2")
    dfs(num + 3, path + "+3")


dfs(1, "1")
dfs(2, "2")
dfs(3, "3")

if answer:
    print(answer)
else:
    print(-1)
