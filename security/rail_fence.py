alphabet = set(list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"))


def encrypt(plain_text: str, key: int) -> str:
    temp = [""] * key
    depth = 0
    for char in plain_text:
        if char not in alphabet:
            continue
        temp[depth] += char
        depth = (depth + 1) % key

    return "".join(temp)


def decrypt(cipher_text: str, key: int) -> str:
    temp = [None] * key
    lens = [len(cipher_text) // key] * key
    remainder = len(cipher_text) % key
    for i in range(remainder):
        lens[i] += 1

    n = 0
    for depth in range(key):
        temp[depth] = cipher_text[n : n + lens[depth]]
        n += lens[depth]

    ml = max(lens)
    plain_text = ""
    for i in range(ml - 1):
        for depth in range(key):
            plain_text += temp[depth][i]

    for depth in range(remainder):
        plain_text += temp[depth][ml - 1]

    return plain_text


plain_text = "meet me after the toga party"
key = 2

print(key)
print(plain_text)

cipher_text = encrypt(plain_text, key)
print(cipher_text)

decrypted = decrypt(cipher_text, key)
print(decrypted)
