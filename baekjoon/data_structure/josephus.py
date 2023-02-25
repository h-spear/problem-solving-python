# https://www.acmicpc.net/problem/1158

# 덱 사용 : python 통과
from collections import deque

n, k = map(int, input().split())
array = [i for i in range(1, n + 1)]

q = deque(array)
print("<", end="")
cnt = 0
while len(q):
    cnt += 1
    if cnt == k:
        if len(q) == 1:
            print(q.popleft(), ">", sep="")
        else:
            print(q.popleft(), end=", ")
        cnt = 0
        continue
    q.append(q.popleft())

# 리스트 구현 : pypy3통과, python 시간초과

# l = len(array)
# i = 0
# print("<", end="")
# while l > 0:
#     if array[i] != 0:
#         cnt += 1
#         if cnt == k:
#             if l == 1:
#                 print(array[i], ">", sep="")
#             else:
#                 print(array[i], end=", ")
#             array[i] = 0
#             l -= 1
#             cnt = 0
#     i = (i + 1) % len(array)
#
