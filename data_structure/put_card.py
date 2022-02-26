# https://www.acmicpc.net/problem/18115

from collections import deque

n = int(input())
tech = list(map(int, input().split()))

curr_deck = [i for i in range(n, 0, -1)]
target = deque()
while tech:
    x = tech.pop()
    item = curr_deck.pop()
    if x == 1:
        target.appendleft(item)
    elif x == 2:
        temp = target.popleft()
        target.appendleft(item)
        target.appendleft(temp)
    elif x == 3:
        target.append(item)

for x in target:
    print(x, end=" ")
