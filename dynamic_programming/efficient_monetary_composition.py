n, m = map(int, input().split())

money_type = []
money = [10001] * 10001
for _ in range(n):
    input_data = int(input())
    money_type.append(input_data)
    money[input_data] = 1

for i in range(min(money_type), m + 1):
    for x in money_type:
        if i + x <= m:
            money[i + x] = min(money[i + x], money[i] + 1)

print(-1 if money[m] == 10001 else money[m])
