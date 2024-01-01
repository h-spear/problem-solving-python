# https://www.acmicpc.net/problem/1747


def get_primes(start, end):
    is_prime = [True] * (end + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(end**0.5) + 1):
        if is_prime[i] == False:
            continue

        j = i + i
        while j <= end:
            is_prime[j] = False
            j += i

    primes = []
    for i in range(start, end + 1):
        if is_prime[i]:
            primes.append(i)

    return primes


def is_palindrome_number(number):
    num_str = str(number)
    length = len(num_str)
    for i in range(length // 2):
        if num_str[i] != num_str[length - i - 1]:
            return False
    return True


if __name__ == "__main__":
    N = int(input())

    for x in get_primes(N, 1003001):
        if is_palindrome_number(x):
            print(x)
            break
