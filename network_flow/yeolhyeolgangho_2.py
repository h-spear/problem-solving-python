# https://www.acmicpc.net/problem/11376
# 한 직원이 두 개의 업무를 한다 -> 단순히 dfs를 두 번씩 호출해주면 됨


def dfs(w):
    if visited[w]:
        return False
    visited[w] = True

    for x in worker[w]:
        if not task[x] or dfs(task[x]):
            task[x] = w
            return True
    return False


answer = 0
visited = None
n, m = map(int, input().split())
worker = [[] for _ in range(n + 1)]
task = [0] * (m + 1)

for i in range(1, n + 1):
    info = list(map(int, input().split()))
    if info[0]:
        worker[i] = info[1:]

for _ in range(2):
    for i in range(1, n + 1):
        visited = [False] * (n + 1)
        if dfs(i):
            answer += 1

print(answer)
