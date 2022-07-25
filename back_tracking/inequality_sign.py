# https://www.acmicpc.net/problem/2529

n = int(input())
signs = list(input().split())
nums = [i for i in range(10)]

minimum = 9987654321
maximum = -1


def back_tracking(idx, s):
    global maximum, minimum
    if idx == n:
        res = int(s)
        if res > maximum:
            maximum = res
        if res < minimum:
            minimum = res
        return

    last = int(s[-1])
    sign = signs[idx]
    for i in range(10):
        if str(i) in s:
            continue

        if sign == "<":
            if last < i:
                back_tracking(idx + 1, s + str(i))
        else:
            if last > i:
                back_tracking(idx + 1, s + str(i))


for i in range(10):
    back_tracking(0, str(i))

print(str(maximum).zfill(n + 1))
print(str(minimum).zfill(n + 1))
