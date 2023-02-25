n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))

array = sorted(array, reverse=True)

for value in array:
    print(value, end=" ")
