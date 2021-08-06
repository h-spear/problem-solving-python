# http://www.acmicpc.net/problem/3190

from collections import deque

n = int(input())
k = int(input())

apples = []
for _ in range(k):
  apple_position = tuple(map(int, input().split()))
  apples.append(apple_position)

l = int(input())

commands = []
for _ in range(l):
  x, cmd = input().split()
  commands.append((int(x), cmd))
commands.sort(reverse=True)

time = 0
direction = 1
snake = deque([(1,1)])

# 북 동 남 서
dr = [-1,0,1,0]
dc = [0,1,0,-1]

while True:
  if len(commands) and time == commands[-1][0]:
    cmd = commands.pop()[1];
    direction = (direction + 3) % 4 if cmd == 'L' else (direction + 1) % 4

  snake_head = snake[-1]
  nr = snake_head[0] + dr[direction]
  nc = snake_head[1] + dc[direction]

  if (nr,nc) in snake or nr > n or nr < 1 or nc > n or nc < 1:
    time += 1
    break

  snake.append((nr,nc))

  if (nr,nc) in apples:
    apples.remove((nr,nc))
  else:
    snake.popleft()
  time += 1

print(time)