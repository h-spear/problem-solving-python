# https://www.acmicpc.net/problem/1072
# 소수점 관련해서 오답이 나왔었음
# 8) z = int(y / x * 100) -> 오답
# 8) z = int(y * 100 / x) -> 정답


x, y = map(int, input().split())
z = int(y * 100 / x)

left = 1
right = 1000000000
answer = -1

while left <= right:
    mid = (left + right) // 2

    if int((y + mid) * 100 / (x + mid)) > z:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)
