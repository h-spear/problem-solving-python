string = input()

result = 0
for i in range(len(string) - 1):
    if string[i] != string[i + 1]:
        result += 1

result //= 2
if string[0] != string[-1]:
    result += 1

print(result)
