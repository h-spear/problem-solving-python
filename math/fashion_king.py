# https://www.acmicpc.net/problem/9375

for tc in range(int(input())):

    n = int(input())

    clothes = dict()
    for _ in range(n):
        name, kind = input().split()
        if kind not in clothes.keys():
            clothes[kind] = []
        clothes[kind].append(name)

    answer = 1
    for kind in clothes.keys():
        answer *= len(clothes[kind]) + 1

    print(answer - 1)
