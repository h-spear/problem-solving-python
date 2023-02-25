number, max_weight = map(int, input().split())
ball_weights = list(map(int, input().split()))

count = 0
for i in range(len(ball_weights)):
    for j in range(i, len(ball_weights)):
        if ball_weights[i] != ball_weights[j]:
            count += 1

print(count)
