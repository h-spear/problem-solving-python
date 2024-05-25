# https://www.acmicpc.net/problem/31866


def main():
    x, y = map(int, input().split())

    if x in [1, 3, 4]:
        x = -1
    if y in [1, 3, 4]:
        y = -1

    if x != -1 and y == -1:
        print(">")
    elif x == -1 and y != -1:
        print("<")

    if x == y:
        print("=")
    elif x == 0:
        if y == 2:
            print(">")
        elif y == 5:
            print("<")
    elif x == 2:
        if y == 0:
            print("<")
        elif y == 5:
            print(">")
    elif x == 5:
        if y == 0:
            print(">")
        elif y == 2:
            print("<")


if __name__ == "__main__":
    main()
