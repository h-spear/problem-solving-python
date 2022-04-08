# 빈도분석을 어렵게 하기 위해 암호문에 나타나는 문자들의 빈도를 균등하게 만듬

alphabet = {char: i for i, char in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
alphabet_rev = {i: char for i, char in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}


def encrypt(plain_text: str, key: str) -> str:
    n = len(plain_text)
    m = len(key)
    k = key * (n // m) + key[: n % m]
    cipher_text = ""
    for i in range(n):
        idx = (alphabet[plain_text[i]] + alphabet[k[i]]) % 26
        cipher_text += alphabet_rev[idx]

    return cipher_text


def decrypt(cipher_text: str, key: str) -> str:
    n = len(cipher_text)
    m = len(key)
    k = key * (n // m) + key[: n % m]
    plain_text = ""
    for i in range(n):
        idx = (alphabet[cipher_text[i]] - alphabet[k[i]]) % 26
        plain_text += alphabet_rev[idx]

    return plain_text


plain_text = "RENAISSANCE"
key = "BAND"

print(key)
print(plain_text)

cipher_text = encrypt(plain_text, key)
print(cipher_text)

decrypted = decrypt(cipher_text, key)
print(decrypted)
