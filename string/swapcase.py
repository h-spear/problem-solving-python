# https://www.acmicpc.net/problem/2744

string = input()
for char in string:
    o = ord(char)
    if o >= ord("a"):
        print(chr(o - ord("a") + ord("A")), end="")
    else:
        print(chr(o - ord("A") + ord("a")), end="")
print()


# print(string.swapcase())
