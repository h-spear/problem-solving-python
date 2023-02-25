# https://www.acmicpc.net/problem/1057

n, a, b = map(int, input().split())

a, b = min(a, b), max(a, b)
li = [i for i in range(1, n + 1)]
flag = False
temp = []
cnt = 0
while not flag:
    temp = []
    cnt += 1
    ll = len(li)
    for i in range(0, len(li), 2):
        if i + 1 >= ll:
            temp.append(li[i])
            break

        if li[i] == a and li[i + 1] == b:
            flag = True
            break
        elif a in li[i : i + 2]:
            temp.append(a)
        elif b in li[i : i + 2]:
            temp.append(b)
        else:
            temp.append(li[i])

    li = temp

if flag:
    print(cnt)
else:
    print(-1)
