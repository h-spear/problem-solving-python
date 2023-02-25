# https://www.acmicpc.net/problem/1049

n, m = map(int, input().split())
packages = []
unit = []
for _ in range(m):
    p, u = map(int, input().split())
    packages.append(p)
    unit.append(u)

mp = min(packages)
mu = min(unit)

candidate1 = (n // 6) * mp + mu * (n % 6)
candidate2 = (n // 6) * mp + mp
candidate3 = mu * n
answer = min(candidate1, candidate2, candidate3)
print(answer)
