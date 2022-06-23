# https://www.acmicpc.net/problem/2166
# 신발끈 공식 : https://ko.wikipedia.org/wiki/%EC%8B%A0%EB%B0%9C%EB%81%88_%EA%B3%B5%EC%8B%9D
# https://ko.wikihow.com/%EB%8B%A4%EA%B0%81%ED%98%95-%EB%84%93%EC%9D%B4-%EA%B5%AC%ED%95%98%EA%B8%B0

n = int(input())
x = []
y = []
for _ in range(n):
    _x, _y = map(int, input().split())
    x.append(_x)
    y.append(_y)
x.append(x[0])
y.append(y[0])

answer = 0
for i in range(n):
    answer += x[i] * y[i + 1]

for i in range(n):
    answer -= y[i] * x[i + 1]

answer /= 2

print(round(abs(answer), 1))
