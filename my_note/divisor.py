# 숫자 e까지 약수 개수를 한 번에 구하는 방법
# https://school.programmers.co.kr/learn/courses/30/lessons/138475

e = 5000000
div = [0] * (e + 1)

for i in range(2, e + 1):
    for j in range(1, min(e // i + 1, i)):
        div[i * j] += 2

for i in range(1, int(e ** 0.5) + 1):
    div[i * i] += 1
