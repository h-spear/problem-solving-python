# https://www.acmicpc.net/problem/2002

n = int(input())
_out = []
_hash = dict()

for i in range(n):
    _hash[input()] = i

for _ in range(n):
    h = _hash[input()]
    _out.append(h)

now = 0
visited = [0] * n
answer = 0
for c in _out:
    visited[c] = 1
    if c != now:
        answer += 1
    else:
        now += 1
        while now < n and visited[now]:
            now += 1

print(answer)
