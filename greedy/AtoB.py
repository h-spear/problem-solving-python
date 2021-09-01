# https://www.acmicpc.net/problem/16953


a, b = map(int, input().split())

result = int(1e9)


def solution(cnt, num):
    global result
    if num == a:
        result = min(result, cnt)
        return
    if num < a:
        return
    if num % 2 == 0:
        solution(cnt + 1, num // 2)
    elif num % 10 == 1:
        solution(cnt + 1, num // 10)


solution(1, b)
print(result if result != int(1e9) else -1)
