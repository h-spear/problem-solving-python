# https://www.acmicpc.net/problem/8979

n, k = map(int, input().split())

medal = []
for _ in range(n):
    medal.append(list(map(int, input().split())))

medal.sort(key=lambda x: (-x[1], -x[2], -x[3]))

for i, m in enumerate(medal):
    if m[0] == k:
        while (
            m[1] == medal[i - 1][1]
            and m[2] == medal[i - 1][2]
            and m[3] == medal[i - 1][3]
        ):
            i -= 1
        print(i + 1)
        break
