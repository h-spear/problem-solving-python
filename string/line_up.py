# https://www.acmicpc.net/problem/11536

n = int(input())
names = []
for _ in range(n):
    names.append(input())

s = sorted(names)

inc = True
dec = True
for i in range(n):
    if names[i] != s[i]:
        inc = False

    if names[i] != s[n - i - 1]:
        dec = False


if inc:
    print("INCREASING")
elif dec:
    print("DECREASING")
else:
    print("NEITHER")
