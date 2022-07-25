# https://www.acmicpc.net/problem/7785

n = int(input())
logs = []
for _ in range(n):
    logs.append(tuple(input().split()))

company = set()
for log in logs:
    name, el = log
    if el == "enter":
        company.add(name)
    else:
        company.remove(name)

company = list(company)
company.sort(reverse=True)

for name in company:
    print(name)
