# https://www.acmicpc.net/problem/12933


def simulate(sound):
    j = 0
    indexes = []
    tmp = []
    for i in range(len(sound)):
        if sound[i] == order[j]:
            j += 1
            tmp.append(i)
            if j == 5:
                j = 0
                indexes.extend(tmp)
                tmp.clear()

    for i in indexes:
        sound[i] = "."
    return len(indexes) != 0


order = ["q", "u", "a", "c", "k"]
sound = list(input())
cnt = 0
while simulate(sound):
    cnt += 1

well_recorded = True
for s in sound:
    if s != ".":
        well_recorded = False
        break

if well_recorded:
    print(cnt)
else:
    print(-1)
