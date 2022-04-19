alphabet = {char: i for i, char in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
alphabet_rev = {i: char for i, char in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}


def mul(A, B):
    la = len(A)
    lac = len(A[0])
    lbc = len(B[0])
    result = [[0] * lbc for _ in range(la)]
    for i in range(la):
        for j in range(lbc):
            temp = 0
            for k in range(lac):
                temp += A[i][k] * B[k][j]
            result[i][j] = temp % 26
    return result


def encrypt(plain_text, key):
    lk = len(key)
    r = len(plain_text) % lk
    plain_text = plain_text.upper()
    if r >= 1:
        plain_text += "X" * (lk - r)

    cipher_text = ""
    for i in range(0, len(plain_text), lk):
        p = []
        for j in range(lk):
            p.append([alphabet[plain_text[i + j]]])

        temp = mul(key, p)
        for j in range(lk):
            cipher_text += alphabet_rev[temp[j][0]]

    return cipher_text


def decrypt(cipher_text, key):
    pass


plain_text = "PAYMOREMONEY"
key = [[17, 17, 5], [21, 18, 21], [2, 2, 19]]
key_inverse = [[4, 9, 15], [15, 17, 6], [24, 0, 17]]

print(key)
print(plain_text)

cipher_text = encrypt(plain_text, key)
print(cipher_text)

decrypted = encrypt(cipher_text, key_inverse)
print(decrypted)
