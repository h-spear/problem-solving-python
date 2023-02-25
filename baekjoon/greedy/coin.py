cost = int(input())
count = 0

money = [500, 100, 50, 10]
for m in money:
    count += cost // m
    cost %= m

print(count)
