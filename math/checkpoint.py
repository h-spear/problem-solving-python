# https://www.acmicpc.net/problem/2981
# 증명 참고 : https://pacific-ocean.tistory.com/224

import sys, math

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
nums = list(int(input()) for _ in range(n))
nums.sort()
diff = []

while len(nums) > 1:
    fi = nums.pop()
    se = nums[-1]
    diff.append(fi - se)

_gcd = 0
while diff:
    if len(diff) == 1:
        _gcd = diff[0]
        break
    fi = diff.pop()
    se = diff.pop()
    _gcd = math.gcd(fi, se)
    diff.append(_gcd)

if n == 1:
    _gcd = nums[0]

answer = set([_gcd])
for i in range(2, int(math.sqrt(_gcd)) + 1):
    if _gcd % i == 0:
        answer.add(i)
        answer.add(_gcd // i)

answer = sorted(list(answer))
print(*answer)
