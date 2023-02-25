# https://www.acmicpc.net/problem/12904
# 연산을 거꾸로 수행하는 방식
# https://chocochip101.tistory.com/entry/%EB%B0%B1%EC%A4%80-12904%EB%B2%88-%ED%8C%8C%EC%9D%B4%EC%8D%AC-A%EC%99%80-B

s = list(input())
t = list(input())

flag = False
while t:
    if t[-1] == "A":
        t.pop()
    elif t[-1] == "B":
        t.pop()
        t.reverse()

    if s == t:
        flag = True
        break

if flag:
    print(1)
else:
    print(0)
