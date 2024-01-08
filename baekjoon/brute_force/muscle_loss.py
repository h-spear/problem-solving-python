# https://www.acmicpc.net/problem/18429

N = -1
K = -1
A = None


def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]


def np(perm, n):
    i = n - 1
    while i > 0 and perm[i - 1] > perm[i]:
        i -= 1

    if i == 0:
        return False

    j = n - 1
    while perm[i - 1] > perm[j]:
        j -= 1

    swap(perm, i - 1, j)

    k = n - 1
    while i < k:
        swap(perm, i, k)
        i += 1
        k -= 1

    return True


def test(order):
    weight = 500
    for i in range(N):
        weight += A[order[i]]
        weight -= K
        if weight < 500:
            return False
    return True


def main():
    global N, A, K

    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    order = [i for i in range(N)]
    answer = 0

    while True:
        if test(order):
            answer += 1
        if not np(order, N):
            break

    print(answer)


if __name__ == "__main__":
    main()
