# https://www.acmicpc.net/problem/5618

n = int(input())
nums = list(map(int, input().split()))
if n == 2:
    nums.append(nums[1])


def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)


#
_gcd = gcd(nums[0], gcd(nums[1], nums[-1]))
answer = []

for i in range(1, (_gcd // 2) + 1):
    if _gcd % i == 0:
        print(i)

print(_gcd)
