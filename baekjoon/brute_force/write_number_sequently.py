# https://www.acmicpc.net/problem/1748

n = int(input())

end = 9
start = 1
answer = 0
while 1:
    if end >= n:
        answer += (n - start + 1) * len(str(n))
        break
    else:
        answer += (end - start + 1) * len(str(end))
        end = end * 10 + 9
        start = start * 10
print(answer)
