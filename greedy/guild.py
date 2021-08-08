n = int(input())
adventures = list(map(int, input().split()))
adventures.sort()

result = 0
user_count = 0

for fear_level in adventures:
    user_count += 1
    if user_count == fear_level:
        result += 1
        user_count = 0

print(result)
