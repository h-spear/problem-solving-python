# https://www.acmicpc.net/problem/3029

cur = list(map(int, input().split(":")))
tar = list(map(int, input().split(":")))

if cur == tar:
    print("24:00:00")
    exit(0)

if cur[2] > tar[2]:
    tar[1] -= 1
    tar[2] += 60
tar[2] -= cur[2]

if tar[1] < 0:
    tar[0] -= 1
    tar[1] += 60

if cur[1] > tar[1]:
    tar[0] -= 1
    tar[1] += 60
tar[1] -= cur[1]

if cur[0] > tar[0]:
    tar[0] += 24
tar[0] -= cur[0]

tar = list(map(str, tar))
answer = ""
for x in tar:
    if len(x) == 1:
        answer += "0"
    answer += x
    answer += ":"

print(answer[:-1])
