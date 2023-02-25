# https://www.acmicpc.net/problem/2559

n, k = map(int, input().split())
T = list(map(int, input().split()))

i = 0
j = k
curr = sum(T[i:j])
answer = curr

while j != n:
    curr += T[j]
    j += 1
    curr -= T[i]
    i += 1

    answer = max(answer, curr)

print(answer)
