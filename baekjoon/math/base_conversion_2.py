hash = {i + 10: x for i, x in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
for i in range(10):
    hash[i] = str(i)

n, b = map(int, input().split())
answer = ""
while n:
    answer += hash[n % b]
    n //= b

print(answer[::-1])
