# https://www.acmicpc.net/problem/2870

n = int(input())
nums = []
for _ in range(n):
    line = input()
    temp = "0"
    for char in line:
        if char.isdigit():
            temp += char
        else:
            if temp != "0":
                nums.append(int(temp))
                temp = "0"

    if temp != "0":
        nums.append(int(temp))

nums.sort()
for num in nums:
    print(num)
