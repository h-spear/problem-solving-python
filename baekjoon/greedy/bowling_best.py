number, max_weight = map(int, input().split())
ball_weights = list(map(int, input().split()))

count = 0
ball_weights_array = [0] * 11
for x in ball_weights:
    ball_weights_array[x] += 1

for i in range(1, max_weight + 1):
    number -= ball_weights_array[i]
    count += number * ball_weights_array[i]

print(count)
