# https://www.acmicpc.net/problem/1713

n = int(input())
t = int(input())
candidates = list(map(int, input().split()))

pic = []
rec = []


def upload_pic(num):
    if len(pic) >= n:
        least = min(rec)
        i = rec.index(least)
        pic.pop(i)
        rec.pop(i)
    pic.append(num)
    rec.append(0)


def nominate(num):
    for i, x in enumerate(pic):
        if x == num:
            rec[i] += 1
            return
    upload_pic(num)


for candidate in candidates:
    nominate(candidate)

print(" ".join(map(str, sorted(pic))))
