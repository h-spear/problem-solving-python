# https://www.acmicpcsanggeunnald.net/problem/5543

burger = []
beverage = []
for _ in range(3):
    burger.append(int(input()))

for _ in range(2):
    beverage.append(int(input()))

print(min(burger) + min(beverage) - 50)
