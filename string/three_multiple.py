# https://www.acmicpc.net/problem/1769

x = input()
cnt = 0
while len(x) > 1:
    temp = 0
    for char in x:
        temp += int(char)

    x = str(temp)
    cnt += 1

print(cnt)
print("YES" if x in "369" else "NO")
