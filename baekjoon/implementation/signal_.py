# https://www.acmicpc.net/problem/16113

n = int(input())
signal = input().replace("#", "1").replace(".", "0")

dict = [
    ["111", "101", "101", "101", "111"],  # 0
    ["000", "000", "000", "000", "000"],  # 1
    ["111", "001", "111", "100", "111"],  # 2
    ["111", "001", "111", "001", "111"],  # 3
    ["101", "101", "111", "001", "001"],  # 4
    ["111", "100", "111", "001", "111"],  # 5
    ["111", "100", "111", "101", "111"],  # 6
    ["111", "001", "001", "001", "001"],  # 7
    ["111", "101", "111", "101", "111"],  # 8
    ["111", "101", "111", "001", "111"],  # 9
]


def decryption(idx):

    if (
        signal[idx]
        == signal[idx + (n // 5)]
        == signal[idx + (n // 5) * 2]
        == signal[idx + (n // 5) * 3]
        == signal[idx + (n // 5) * 4]
        == "0"
    ):
        return 1

    if (
        signal[idx]
        == signal[idx + (n // 5)]
        == signal[idx + (n // 5) * 2]
        == signal[idx + (n // 5) * 3]
        == signal[idx + (n // 5) * 4]
        == "1"
    ):
        if idx + 1 == n // 5 or (
            signal[idx + 1]
            == signal[idx + (n // 5) + 1]
            == signal[idx + (n // 5) * 2 + 1]
            == signal[idx + (n // 5) * 3 + 1]
            == signal[idx + (n // 5) * 4 + 1]
            == "0"
        ):
            print(1, end="")
            return 2

    for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        cnt = 0
        for j in range(5):
            if signal[idx + (n // 5) * j : idx + (n // 5) * j + 3] == dict[i][j]:
                cnt += 1
        if cnt == 5:
            print(i, end="")
            return 3


i = 0
while i < n // 5:
    i += decryption(i)
