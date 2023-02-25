# https://www.acmicpc.net/problem/15904

abbreviation = "UCPC"
string = input()
i = 0
for char in string:
    if char == abbreviation[i]:
        i += 1
        if i == 4:
            break

if i == 4:
    print("I love UCPC")
else:
    print("I hate UCPC")
