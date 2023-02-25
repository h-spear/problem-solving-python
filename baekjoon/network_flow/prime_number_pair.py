# https://www.acmicpc.net/problem/1017
# 홀수, 짝수로 그룹을 나누어야 함.

from collections import defaultdict


def eratosthenes():
    is_prime[0], is_prime[1] = False, False

    for i in range(2, int(MAX_PRIME_NUMBER ** 0.5) + 1):
        if not is_prime[i]:
            continue
        j = 2
        while i * j <= MAX_PRIME_NUMBER:
            is_prime[i * j] = False
            j += 1
    return is_prime


def dfs(num):
    if visit[num]:
        return False
    visit[num] = True

    for nnum in graph[num]:
        if nnum in [candidate, first_select]:
            continue
        if not matched[nnum] or dfs(matched[nnum]):
            matched[nnum] = num
            return True

    return False


MAX_PRIME_NUMBER = 2010
is_prime = [True] * (MAX_PRIME_NUMBER + 1)
graph = defaultdict(list)
answer = []
odds = []
evens = []
matched = None
visit = None
n = int(input())
nums = list(map(int, input().split()))
first_select = nums[0]
candidate = 0
all_pair = len(nums) // 2

# 소수 구하기
eratosthenes()

# 그래프 생성
for num in nums:
    if num & 1:
        odds.append(num)
    else:
        evens.append(num)

for odd in odds:
    for even in evens:
        if is_prime[odd + even]:
            graph[odd].append(even)
            graph[even].append(odd)

# 이분 매칭
for x in graph[first_select]:
    matched = defaultdict(int)
    candidate = x
    counter = 1
    for odd in odds:
        visit = [False] * (MAX_PRIME_NUMBER + 1)
        if odd in [candidate, first_select]:
            continue
        if dfs(odd):
            counter += 1
    if counter == all_pair:
        answer.append(x)

# 결과 출력
answer.sort()
if not answer:
    print(-1)
else:
    print(*answer)
