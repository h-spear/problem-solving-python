# 파이썬 내장 라이브러리
from itertools import product
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement

data = ["A", "B", "C"]

# permutations(p[,r]) : 순열
# P개 중 n개를 선택하여 만든 순열. tuple
print(list(permutations(data, 2)))

# product() : 데카르트 곱
# P개 중 n개를 중복을 허용하게 선택하여 만든 순열. tuple
print(list(product(data, repeat=2)))

# combinations(p, r): 조합
# p개 중 r개 선택하는 조합. tuple
print(list(combinations(data, 2)))

# combinations_with_replacement(p,r) : 조합
# p개 중 r개 선택하는 중복을 허용하는 조합. tuple
print(list(combinations_with_replacement(data, 2)))
