# https://www.acmicpc.net/problem/9242

hash = {
    (
        "***",
        "* *",
        "* *",
        "* *",
        "***",
    ): "0",
    (
        "  *",
        "  *",
        "  *",
        "  *",
        "  *",
    ): "1",
    (
        "***",
        "  *",
        "***",
        "*  ",
        "***",
    ): "2",
    (
        "***",
        "  *",
        "***",
        "  *",
        "***",
    ): "3",
    (
        "* *",
        "* *",
        "***",
        "  *",
        "  *",
    ): "4",
    (
        "***",
        "*  ",
        "***",
        "  *",
        "***",
    ): "5",
    (
        "***",
        "*  ",
        "***",
        "* *",
        "***",
    ): "6",
    (
        "***",
        "  *",
        "  *",
        "  *",
        "  *",
    ): "7",
    (
        "***",
        "* *",
        "***",
        "* *",
        "***",
    ): "8",
    (
        "***",
        "* *",
        "***",
        "  *",
        "***",
    ): "9",
}

fail_msg = "BOOM!!"
success_msg = "BEER!!"
code = []
for _ in range(5):
    code.append(input())


def fn():
    if (len(code[0]) + 1) % 4 != 0:
        print(fail_msg)
    else:
        n = (len(code[0]) + 1) // 4
        temp = ""
        for i in range(0, len(code[0]), 4):
            ch = (
                code[0][i : i + 3],
                code[1][i : i + 3],
                code[2][i : i + 3],
                code[3][i : i + 3],
                code[4][i : i + 3],
            )
            if ch not in hash:
                print(fail_msg)
                return
            temp += hash[ch]

        if int(temp) % 6 == 0:
            print(success_msg)
        else:
            print(fail_msg)


fn()
