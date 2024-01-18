# https://www.acmicpc.net/problem/2785


def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    answer = 0
    right = N - 1
    for left in range(0, N):
        if left >= right:
            break

        while left < right and L[left] > 0:
            right -= 1
            L[left] -= 1
            answer += 1

    print(answer)


if __name__ == "__main__":
    main()
