# https://www.acmicpc.net/problem/9506


def find_divisor(num):
    divisor = []
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            divisor.append(i)

            if i == num // i:
                continue

            divisor.append(num // i)
    divisor.sort()
    return divisor


def find_perfect_number(num):
    divisor = find_divisor(num)
    summation = sum(divisor[:-1])
    if num == summation:
        print("{} = {}".format(num, 1), end="")

        for i in range(1, len(divisor) - 1):
            print(" + {}".format(divisor[i]), end="")
    else:
        print("{} is NOT perfect.".format(num), end="")
    print()


while 1:
    n = int(input())
    if n == -1:
        break
    find_perfect_number(n)
