n = int(input())
score = []
for _ in range(n):
    score.append(int(input()))

score.reverse()
answer = 0
for i in range(1, n):
    if score[i] >= score[i - 1]:
        answer += score[i] - score[i - 1] + 1
        score[i] = score[i - 1] - 1

print(answer)
