# https://www.acmicpc.net/problem/10815


def find(A, num):
    left, right = 0, len(A) - 1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] == num:
            return 1
        elif A[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    return 0


n = int(input())
has = list(map(int, input().split()))
has.sort()
m = int(input())
cards = list(map(int, input().split()))


for card in cards:
    print(find(has, card), end=" ")
