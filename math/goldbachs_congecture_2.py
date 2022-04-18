# https://www.acmicpc.net/problem/6588

m = 1000000
prime = [True] * (m + 1)
prime[0], prime[1] = False, False

for i in range(2, int(m ** 0.5) + 1):
    if not prime[i]:
        continue

    j = 2
    while i * j <= m:
        prime[i * j] = False
        j += 1


def func(even):
    for i in range(1, even // 2 + 1, 2):
        if prime[i] and prime[even - i]:
            print("{} = {} + {}".format(even, i, even - i))
            return

    print("Goldbach's conjecture is wrong.")


while 1:
    n = int(input())
    if n == 0:
        break

    func(n)
