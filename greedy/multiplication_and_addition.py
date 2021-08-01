input_data = list(map(int, list(input())))

result = 0

for x in input_data:
    if x <= 1 or result <= 1:
        result += x
    else:
        result *= x


print(result)
