# https://www.acmicpc.net/problem/1357


def rev(x: str) -> int:
    return int(x[::-1])


x, y = input().split()
temp = rev(x) + rev(y)
temp = str(temp)
print(rev(temp))
