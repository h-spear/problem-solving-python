from collections import deque

n = int(input())
card = [i for i in range(n, 0, -1)]
card = deque(card)
discard = []

while len(card) > 1:
    item = card.pop()
    discard.append(item)

    item = card.pop()
    card.appendleft(item)

discard.append(card.pop())
print(*discard)
