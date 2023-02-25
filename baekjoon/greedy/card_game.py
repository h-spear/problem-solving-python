n, m = map(int, input().split())
result = 0

cards = []
for i in range(n):
    row = list(map(int, input().split()))
    row.sort()
    cards.append(row)

for row in cards:
    card = row[0]
    if card > result:
        result = card

print(result)
