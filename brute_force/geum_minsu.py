# https://www.acmicpc.net/problem/1527


def geum_minsu(num=0, depth=0):
    global answer, lower, upper

    if depth == 10:
        return

    if num >= lower and num <= upper:
        answer += 1

    geum_minsu(num * 10 + 4, depth + 1)
    geum_minsu(num * 10 + 7, depth + 1)


answer = 0
lower, upper = map(int, input().split())
geum_minsu()
print(answer)
