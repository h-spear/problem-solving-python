# https://www.youtube.com/watch?v=qJ_ft3Spcxc&list=PLN3yisVKGPfhrB0k5wUhF74MVPxzvgGB4
# https://www.youtube.com/watch?v=-PzOmhPYF88&list=PLN3yisVKGPfhrB0k5wUhF74MVPxzvgGB4&index=2
# https://velog.io/@gopas777/%EB%B0%B1%EC%A4%80-9249-python
# O(nlogn)

s = "ababc"

n = len(s)
suffix_array = [i for i in range(n)]
g = [0] * (n + 1)
ng = [0] * (n + 1)

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

print(suffix_array)
print(lcp)
