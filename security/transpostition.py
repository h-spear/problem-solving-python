import math


def encrypt(plain_text: str, key: list) -> str:
    lt = len(plain_text)
    c = len(key)
    r = math.ceil(lt / c)
    matrix = [[" "] * c for _ in range(r)]
    if len(plain_text) != r * c:
        plain_text += "x" * (r * c - len(plain_text))

    idx = 0
    for i in range(r):
        for j in range(c):
            matrix[i][j] = plain_text[idx]
            idx += 1

    cipher_text = ""
    frag = []
    for j in range(c):
        temp = ""
        for i in range(r):
            temp += matrix[i][j]
        frag.append((key[j], temp))
    frag.sort()

    for _, s in frag:
        cipher_text += s

    return cipher_text


def decrypt(cipher_text: str, key: int) -> str:
    lt = len(cipher_text)
    c = len(key)
    r = lt // c
    matrix = [[" "] * c for _ in range(r)]

    idx = 0
    for j in range(c):
        for i in range(r):
            matrix[i][j] = cipher_text[idx]
            idx += 1

    temp = [[" "] * c for _ in range(r)]
    for j in range(c):
        for i in range(r):
            temp[i][j] = matrix[i][key[j] - 1]

    plain_text = ""
    for row in temp:
        plain_text += "".join(row)
    return plain_text


plain_text = "attackpostponeduntiltwoamxyz"
key = [4, 3, 1, 2, 5, 6, 7]

print(key)
print(plain_text)

cipher_text = encrypt(plain_text, key)
print(cipher_text)

decrypted = decrypt(cipher_text, key)
print(decrypted)
