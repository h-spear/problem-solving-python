# https://www.acmicpc.net/problem/13264

s = list(input())
n = len(s)

g = [0] * (n + 1)
ng = [0] * (n + 1)
s_array = [i for i in range(n)]

for i in range(n):
    g[i] = ord(s[i])


g[n] = -1
ng[0] = s_array[0]
ng[n] = -1

t = 1
while t < n:
    s_array.sort(key=lambda x: (g[x], g[min(x + t, n)]))

    for i in range(1, n):
        p, q = s_array[i - 1], s_array[i]
        if g[p] != g[q] or g[min(p + t, n)] != g[min(q + t, n)]:
            ng[q] = ng[p] + 1
        else:
            ng[q] = ng[p]

    t *= 2
    g = ng[:]

for x in s_array:
    print(x)
