# https://www.acmicpc.net/problem/9248

s = list(input())
n = len(s)
g = [0] * (n + 1)
ng = [0] * (n + 1)
suffix_array = [i for i in range(n)]

for i in range(n):
    g[i] = ord(s[i])

g[n] = -1
ng[suffix_array[0]] = 0
ng[n] = -1

t = 1
while t < n:
    suffix_array.sort(key=lambda x: (g[x], g[min(x + t, n)]))

    for i in range(1, n):
        p, q = suffix_array[i - 1], suffix_array[i]
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
    p = suffix_array[k - 1]

    while i + length < n and p + length < n and s[i + length] == s[p + length]:
        length += 1
    lcp[k] = length

    if length:
        length -= 1


for x in suffix_array:
    print(x + 1, end=" ")
print()
lcp[0] = "x"
print(*lcp)
