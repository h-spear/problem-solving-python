# https://www.acmicpc.net/problem/4153


def isRight(a, b, c):
    if a ** 2 + b ** 2 == c ** 2:
        return True


while True:
    data = list(map(int, input().split()))
    data.sort()
    if data.count(0) == 3:
        break
    print("right" if isRight(data[0], data[1], data[2]) else "wrong")
