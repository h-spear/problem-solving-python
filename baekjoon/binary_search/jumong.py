# https://www.acmicpc.net/problem/1940

from bisect import bisect_left, bisect_right

n = int(input())
m = int(input())
arr = list(map(int, input().split()))

arr.sort()

i = 0
answer = 0
now = arr[i]
while i < n:
    j = bisect_right(arr, arr[i])
    mat1_cnt = j - i

    req = m - arr[i]
    mat2_cnt = bisect_right(arr, req) - bisect_left(arr, req)
    answer += mat1_cnt * mat2_cnt
    i = j

print(answer // 2)
