# https://www.acmicpc.net/problem/4446

hash = {
    "a": "e",
    "i": "o",
    "y": "u",
    "e": "a",
    "o": "i",
    "u": "y",
    "b": "p",
    "p": "b",
    "k": "v",
    "v": "k",
    "x": "j",
    "j": "x",
    "z": "q",
    "q": "z",
    "n": "t",
    "t": "n",
    "h": "s",
    "s": "h",
    "d": "r",
    "r": "d",
    "c": "l",
    "l": "c",
    "w": "m",
    "m": "w",
    "g": "f",
    "f": "g",
    "A": "E",
    "I": "O",
    "Y": "U",
    "E": "A",
    "O": "I",
    "U": "Y",
    "B": "P",
    "P": "B",
    "K": "V",
    "V": "K",
    "X": "J",
    "J": "X",
    "Z": "Q",
    "Q": "Z",
    "N": "T",
    "T": "N",
    "H": "S",
    "S": "H",
    "D": "R",
    "R": "D",
    "C": "L",
    "L": "C",
    "W": "M",
    "M": "W",
    "G": "F",
    "F": "G",
}

while 1:
    try:
        string = input()
        for char in string:
            if char in hash:
                print(hash[char], end="")
            else:
                print(char, end="")
        print()
    except:
        break
