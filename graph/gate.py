def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


g = int(input())
p = int(input())

parent = [0] * (g + 1)
for i in range(g + 1):
    parent[i] = i


gate_info = []
for _ in range(p):
    gate_info.append(int(input()))

result = 0
for info in gate_info:
    gate = find(parent, info)
    if gate == 0:
        break
    union(parent, gate, gate - 1)
    result += 1

print(result)
