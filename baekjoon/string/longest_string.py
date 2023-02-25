# https://www.acmicpc.net/problem/3033
# suffix array & lcp

l = int(input())
s = list(input())

suffix_array = [i for i in range(l)]
g = [0] * (l + 1)
ng = [0] * (l + 1)

for i in range(l):
    g[i] = ord(s[i])

g[l] = -1
ng[suffix_array[0]] = 0
ng[l] = -1

t = 1
while t < l:
    suffix_array.sort(key=lambda x: (g[x], g[min(x + t, l)]))

    for i in range(1, l):
        p, q = suffix_array[i - 1], suffix_array[i]
        if g[p] != g[q] or g[min(p + t, l)] != g[min(q + t, l)]:
            ng[q] = ng[p] + 1
        else:
            ng[q] = ng[p]

    t *= 2
    g = ng[:]

lcp = [0] * l
length = 0
flag = True
for i in range(l):
    k = g[i]

    if k >= l:
        flag = False
        break

    if k == 0:
        continue
    p = suffix_array[k - 1]

    while i + length < l and p + length < l and s[i + length] == s[p + length]:
        length += 1
    lcp[k] = length

    if length:
        length -= 1

if flag:
    print(max(lcp))
else:
    print(0)
