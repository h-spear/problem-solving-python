input_data = list(input())
input_data.sort()

string = ""
number = 0

for i in range(len(input_data)):
    x = input_data[i]
    if ord(x) >= 48 and ord(x) <= 57:
        number += int(x)
    else:
        string += x


print(string + str(number))
