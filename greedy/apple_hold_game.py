# https://www.acmicpc.net/problem/2828

n, m = map(int, input().split())
j = int(input())
apple_position = []
answer = 0
for _ in range(j):
    apple_position.append(int(input()))

b_position = 1
for pos in apple_position:
    if b_position + m - 1 < pos:
        answer += pos - (b_position + m - 1)
        b_position = pos - m + 1
    elif b_position > pos:
        answer += b_position - pos
        b_position = pos

print(answer)
