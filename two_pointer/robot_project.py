# https://www.acmicpc.net/problem/3649

import sys

input = lambda: sys.stdin.readline().rstrip()

while 1:
    try:
        x = int(input()) * 10000000
        n = int(input())
        A = []
        for _ in range(n):
            A.append(int(input()))
        A.sort()

        def solve():
            i = 0
            j = n - 1
            while i < j:
                if A[i] >= x:
                    break

                if A[i] + A[j] == x:
                    print("yes", A[i], A[j])
                    return
                elif A[i] + A[j] > x:
                    j -= 1
                else:
                    i += 1
            print("danger")

        solve()
    except:
        break
