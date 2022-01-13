# https://www.acmicpc.net/problem/3048


def move():
    global result
    will = []
    for i in range(len(result) - 1):
        if (result[i] in first) and (result[i + 1] in second):
            will.append(i)
    for w in will:
        result[w], result[w + 1] = result[w + 1], result[w]


n1, n2 = map(int, input().split())

first = list(input())
second = list(input())
result = list(reversed(first))

for x in second:
    result.append(x)

for _ in range(int(input())):
    move()

print("".join(result))
