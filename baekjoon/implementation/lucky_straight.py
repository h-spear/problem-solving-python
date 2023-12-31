# https://www.acmicpc.net/problem/18406

input_data = list(map(int, list(input())))

length = len(input_data)

sum_left = sum(input_data[0 : length // 2])
sum_right = sum(input_data[length // 2 :])

print("LUCKY" if sum_left == sum_right else "READY")
