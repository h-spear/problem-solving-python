# https://www.acmicpc.net/problem/1010

# 조합 combination
# n+1Cr+1 = nCr + nCr+1
# nC0 = nCn = 1

for tc in range(int(input())):
    target_r, target_n = map(int, input().split())

    comb = [[0] * 31 for _ in range(31)]

    for n in range(target_n + 1):
        for r in range(target_r + 1):
            if r == 0 or n == r:
                comb[n][r] = 1
            else:
                comb[n][r] = comb[n - 1][r - 1] + comb[n - 1][r]

    print(comb[target_n][target_r])
