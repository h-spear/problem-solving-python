# 최댓값 지정하는 법

# 방법1
import sys

mx = sys.maxsize
mn = -sys.maxsize
print(sys.maxsize)  # 2^63 - 1

# 방법2
mx = float("inf")
mn = float("-inf")
