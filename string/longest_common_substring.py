# https://www.acmicpc.net/problem/9249

a = input()
b = input()
s = a + "1" + b
n = len(s)
la = len(a)
lb = len(b)

g = [0] * (n + 1)
ng = [0] * (n + 1)
s_arr = [i for i in range(n)]

for i in range(n):
    g[i] = ord(s[i])

g[n] = -1
ng[s_arr[0]] = 0
ng[n] = -1

t = 1
while t < n:
    s_arr.sort(key=lambda x: (g[x], g[min(x + t, n)]))

    for i in range(1, n):
        p, q = s_arr[i - 1], s_arr[i]
        if g[p] != g[q] or g[min(p + t, n)] != g[min(q + t, n)]:
            ng[q] = ng[p] + 1
        else:
            ng[q] = ng[p]

    t *= 2
    g = ng[:]

lcp = [0] * n
length = 0
for i in range(n):
    k = g[i]
    if k == 0:
        continue
    p = s_arr[k - 1]

    while i + length < n and p + length < n and s[i + length] == s[p + length]:
        length += 1
    lcp[k] = length

    if length:
        length -= 1

#######
m = -1
idx = -1
for i, v in enumerate(lcp):
    if 0 <= s_arr[i - 1] + v - 1 < la and la < s_arr[i] + v - 1 < n:
        if m < v:
            m = v
            idx = i
    if 0 <= s_arr[i] + v - 1 < la and la < s_arr[i - 1] + v - 1 < n:
        if m < v:
            m = v
            idx = i

idx = s_arr[idx]
print(m)
print(s[idx : idx + m])
