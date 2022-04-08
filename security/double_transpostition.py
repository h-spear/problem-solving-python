def encrypt(plain_text: str, key: list) -> str:
    row_key, col_key = key[0], key[1]
    r, c = len(row_key), len(col_key)
    n = len(plain_text)
    matrix = [[" "] * c for _ in range(r)]

    idx = 0
    for i in range(r):
        for j in range(c):
            if idx >= n:
                matrix[i][j] = "x"
                continue
            matrix[i][j] = plain_text[idx]
            idx += 1

    row_changed = [[" "] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            row_changed[i][j] = matrix[row_key[i] - 1][j]

    col_changed = [[" "] * c for _ in range(r)]
    for j in range(c):
        for i in range(r):
            col_changed[i][j] = row_changed[i][col_key[j] - 1]

    cipher_text = ""
    for i in range(r):
        for j in range(c):
            cipher_text += col_changed[i][j]

    return cipher_text


def decrypt(cipher_text: str, key: int) -> str:
    row_key, col_key = key[0], key[1]
    r, c = len(row_key), len(col_key)
    n = len(cipher_text)
    matrix = [[" "] * c for _ in range(r)]

    idx = 0
    for i in range(r):
        for j in range(c):
            matrix[i][j] = cipher_text[idx]
            idx += 1

    row_changed = [[" "] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            row_changed[row_key[i] - 1][j] = matrix[i][j]

    col_changed = [[" "] * c for _ in range(r)]
    for j in range(c):
        for i in range(r):
            col_changed[i][col_key[j] - 1] = row_changed[i][j]

    plain_text = ""
    for i in range(r):
        for j in range(c):
            plain_text += col_changed[i][j]

    return plain_text


plain_text = "attackxatxdawn"
key = [[3, 5, 1, 4, 2], [1, 3, 2]]

print(key)
print(plain_text)

cipher_text = encrypt(plain_text, key)
print(cipher_text)

decrypted = decrypt(cipher_text, key)
print(decrypted)
