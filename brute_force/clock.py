# https://www.acmicpc.net/problem/18312

n, k = input().split()

cnt = 0
for i in range(int(n) + 1):
    for j in range(60):
        for _k in range(60):
            now = (
                ("0" if i < 10 else "")
                + str(i)
                + ("0" if j < 10 else "")
                + str(j)
                + ("0" if _k < 10 else "")
                + str(_k)
            )
            if now.find(k) == -1:
                continue
            cnt += 1

print(cnt)
