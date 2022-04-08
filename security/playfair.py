alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def convert_text_to_diagraphs(text: str) -> str:
    for i in range(0, len(text) + 1, 2):
        if i < len(text) - 1:
            if text[i] == text[i + 1]:
                text = text[: i + 1] + "X" + text[i + 1 :]

    if len(text) % 2 != 0:
        text = text[:] + "X"

    return text


def generate_key_matrix(key: str) -> list:
    key_matrix = [[" "] * 5 for _ in range(5)]
    used = set()

    temp = []
    for char in key:
        if char == "J":
            char = "I"
        if char in used:
            continue

        temp.append(char)
        used.add(char)

    for char in alphabet:
        if char == "J":
            continue
        if char not in used:
            temp.append(char)

    k = 0
    for i in range(5):
        for j in range(5):
            key_matrix[i][j] = temp[k]
            k += 1

    return key_matrix


def substitution(char_2: str, key_matrix: list, use_encrypt: bool = True) -> int:
    x1, y1, x2, y2 = 0, 0, 0, 0
    for i in range(5):
        for j in range(5):
            if key_matrix[i][j] == char_2[0]:
                x1, y1 = i, j
            if key_matrix[i][j] == char_2[1]:
                x2, y2 = i, j

    result = ""

    if x1 == x2:
        ny1 = (y1 + 1) % 5 if use_encrypt else (y1 - 1) % 5
        ny2 = (y2 + 1) % 5 if use_encrypt else (y2 - 1) % 5
        result += key_matrix[x1][ny1]
        result += key_matrix[x1][ny2]
    elif y1 == y2:
        nx1 = (x1 + 1) % 5 if use_encrypt else (x1 - 1) % 5
        nx2 = (x2 + 1) % 5 if use_encrypt else (x2 - 1) % 5
        result += key_matrix[nx1][y1]
        result += key_matrix[nx2][y1]
    else:
        result += key_matrix[x1][y2]
        result += key_matrix[x2][y1]

    return result


def encrypt(plain_text: str, key: str) -> str:
    diagraphs = convert_text_to_diagraphs(plain_text)
    key_matrix = generate_key_matrix(key)
    cipher_text = ""
    for i in range(0, len(plain_text), 2):
        char_2 = diagraphs[i : i + 2]
        cipher_text += substitution(char_2, key_matrix)

    return cipher_text


plain_text = "COMPUTER"
key = "SCIENCE"

print(key)
print(plain_text)

cipher_text = encrypt(plain_text, key)
print(cipher_text)
