# https://programmers.co.kr/learn/courses/30/lessons/12977

import math
from itertools import combinations

def solution(nums):
    # 에라토스테네스
    end = max(nums) * 3
    A = [1 for i in range(end + 1)]
    A[0], A[1] = 0, 0

    for i in range(2, int(math.sqrt(end) + 1)):
        if A[i] == 1:
            # i가 소수인 경우 i를 제외한 i의 모든 배수 false
            j = 2
            while i * j <= end:
                A[i * j] = 0
                j += 1
                
    answer = 0
    for x,y,z in combinations(nums, 3):
        answer += A[x+y+z]

    return answer