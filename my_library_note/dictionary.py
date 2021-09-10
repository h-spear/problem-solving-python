from collections import Counter
from collections import defaultdict
from collections import OrderedDict

dict1 = defaultdict(int)  # 형식 입력해야함
dict1["A"] = 1
dict1["B"] = 2
print(dict1)
dict1["C"] += 3
print(dict1)


list = [1, 2, 3, 4, 5, 5, 5, 6, 6, 6, 6, 7]
dict2 = Counter(list)
print(dict2)

# Counter - most_common(n)
# 가장 빈도가 높은 n개의 요소(key, value) 추출
print(dict2.most_common(1))


# 파이썬 3.6 이전
dict3 = OrderedDict({"banana": 3, "apple": 4, "pear": 1, "orange": 2})
print(dict3)  # 입력 순서가 유지되는 dictionary
