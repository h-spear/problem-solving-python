# https://www.acmicpc.net/problem/15312

stroke_cnt = [
    3,
    2,
    1,
    2,
    3,
    3,
    2,
    3,
    3,
    2,
    2,
    1,
    2,
    2,
    1,
    2,
    2,
    2,
    1,
    2,
    1,
    1,
    1,
    2,
    2,
    1,
]
hash = {
    alphabet: stroke_cnt[i] for i, alphabet in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
}
a = input()
b = input()
l = len(a)
container = []
for i in range(l):
    container.append(hash[a[i]])
    container.append(hash[b[i]])

while len(container) > 2:
    temp = []
    for i in range(len(container) - 1):
        num = (container[i] + container[i + 1]) % 10
        temp.append(num)

    container = temp

print("".join(list(map(str, container))))
