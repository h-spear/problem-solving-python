# 최초의 치환 암호
# 쥴리어스 시이저에 의해 개발

alphabet = {char: i for i, char in enumerate("abcdefghijklmnopqrstuvwxyz")}
alphabet_rev = {i: char for i, char in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}


def encrypt(plain_text: str, key: int) -> str:
    cipher_text = ""
    for char in plain_text:
        if char not in alphabet:
            cipher_text += char
            continue
        i = alphabet[char]
        idx = (i + key) % 26
        cipher_text += alphabet_rev[idx]

    return cipher_text


def decrypt(cipher_text: str, key: int) -> str:
    plain_text = ""
    for char in cipher_text:
        char = char.lower()
        if char not in alphabet:
            plain_text += char
            continue
        i = alphabet[char]
        idx = (i - key) % 26
        plain_text += alphabet_rev[idx].lower()

    return plain_text


plain_text = "meet me after the toga party"
key = 3

print(key)
print(plain_text)

cipher_text = encrypt(plain_text, key)
print(cipher_text)

decrypted = decrypt(cipher_text, key)
print(decrypted)
