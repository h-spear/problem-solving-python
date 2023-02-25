# https://www.acmicpc.net/problem/2608

_hash = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
    "IV": 4,
    "IX": 9,
    "XL": 40,
    "XC": 90,
    "CD": 400,
    "CM": 900,
}
rev_hash = {_hash[romestr]: romestr for romestr in _hash}
unit = [num for num in rev_hash]
unit.sort(reverse=True)


def rome_to_arabia(romestr):
    lr = len(romestr)
    num = 0

    i = 0
    while i < lr:
        if i + 1 < lr:
            r = romestr[i : i + 2]
            if r in _hash:
                num += _hash[r]
                i += 2
                continue

        r = romestr[i]
        if r in _hash:
            num += _hash[r]
        i += 1

    return num


def arabia_to_rome(num):
    romestr = ""
    i = 0
    while num:
        u = unit[i]
        if num >= u:
            romestr += rev_hash[u]
            num -= u
        else:
            i += 1
    return romestr


str1 = input()
str2 = input()
num = rome_to_arabia(str1) + rome_to_arabia(str2)
print(num)
print(arabia_to_rome(num))
