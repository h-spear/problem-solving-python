# https://www.acmicpc.net/problem/13417

from collections import deque

for tc in range(int(input())):
    n = int(input())
    cards = input().split()
    q = deque([cards[0]])

    for i in range(1, n):
        card = cards[i]
        if q[0] >= card:
            q.appendleft(card)
        else:
            q.append(card)

    print("".join(q))
