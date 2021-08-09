import bisect

n, x = map(int, input().split())
array = list(map(int, input().split()))

count = bisect.bisect_right(array, x) - bisect.bisect_left(array, x)
print(-1 if count == 0 else count)
