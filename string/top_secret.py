# https://www.acmicpc.net/problem/11365

while 1:
    cipher = input()
    if cipher == "END":
        break
    print(cipher[::-1])
