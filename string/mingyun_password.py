# https://www.acmicpc.net/problem/9933

n = int(input())
candidates = set()
pwd_list = []
for _ in range(n):
    input_data = input()
    pwd_list.append(input_data)
    candidates.add(input_data[::-1])

for pwd in pwd_list:
    if pwd in candidates:
        print(len(pwd), pwd[len(pwd) // 2])
        break
