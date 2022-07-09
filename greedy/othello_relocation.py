# https://www.acmicpc.net/problem/13413

from collections import Counter

for tc in range(int(input())):
    n = int(input())
    state = list(input())
    target = list(input())

    s_counter = Counter(state)
    t_counter = Counter(target)

    diff = abs(s_counter["B"] - t_counter["B"])
    answer = diff
    temp = 0
    # 개수 먼저 맞추기
    for i in range(n):
        if state[i] != target[i]:
            temp += 1

    print(diff + (temp - diff) // 2)
