# 소수 판별 알고리즘
import math
from collections import Counter

# O(N)


def is_prime_number_1(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


# O(N^(1/2))
def is_prime_number_2(x):
    # 2 ~ x의 제곱끈까지의 모든 수
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


# 에라토스테네스의 체 O(NlogN)
# 여러 개의 소수를 판별해야 할 때 효율적
# 메모리가 많이 필요하다는 단점.
def find_prime_numbers(start, end):
    A = [True for i in range(end + 1)]
    A[0], A[1] = False, False

    for i in range(2, int(math.sqrt(end) + 1)):
        if A[i] == True:
            # i가 소수인 경우 i를 제외한 i의 모든 배수 false
            j = 2
            while i * j <= end:
                A[i * j] = False
                j += 1

    # 소수 출력
    for i in range(start, end + 1):
        if A[i]:
            print(i, end=" ")

    # 소수의 개수
    print()
    print(A[start : end + 1].count(True))
    print(Counter(A[start : end + 1])[True])  # Collections.Counter 이용


find_prime_numbers(1000, 10000)
