n = int(input())
array = list(map(int, input().split()))

def findFixedPoint(left, right):
  while left < right:
    mid = (left+right)//2
    if array[mid] == mid:
      return mid
    elif array[mid] < mid:
      left = mid + 1
    else:
      right = mid
  return -1

print(findFixedPoint(0,len(array)- 1))