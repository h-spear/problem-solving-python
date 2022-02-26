# https://www.acmicpc.net/problem/11656

s = input()
result = []
for i in range(len(s)):
    result.append(s[i:])
result.sort()
for x in result:
    print(x)
