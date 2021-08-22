import sys
from collections import deque

input = sys.stdin.readline
for tc in range(int(input())):
  n, m =map(int, input().split())
  data = list(map(int, input().split()))
  q = deque()

  for i in range(len(data)):
    q.append((data[i], (1 if i == m else 0)))

  data.sort(reverse=True)
  data = deque(data)
  cnt = 1
  while True:
    prior = data[0]

    if prior == q[0][0] and q[0][1] == 1:
      break

    elif prior != q[0][0]:
      q.append(q.popleft())

    elif prior == q[0][0]:
      q.popleft()
      data.popleft()
      cnt += 1

  print(cnt)