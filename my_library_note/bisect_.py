# bisect
# '정렬된 배열'에서 특정한 원소를 찾을 때 효율적 O(logN)
from bisect import bisect_left
from bisect import bisect_right


# 정렬된 배열에서 left_value 이상, right_value이하인 데이터의 개수를 반환
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index


a = [1, 2, 4, 4, 8, 16, 32]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))
print(count_by_range(a, 3, 8))
