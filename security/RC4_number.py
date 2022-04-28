import random

bits = 256


def key_schedling(key):
    # initialize
    key_length = len(key)
    S = [i for i in range(bits)]
    T = [key[i % key_length] for i in range(bits)]

    # key scheduling
    j = 0
    for i in range(bits):
        j = (j + S[i] + T[i]) % bits
        S[i], S[j] = S[j], S[i]

    return S


def encrypt(message, key):
    i = 0
    j = 0
    S = key_schedling(key)
    stream_key = []
    cipher_text = []

    for k in range(len(message)):
        i = (i + 1) % bits
        j = (j + S[i]) % bits
        S[i], S[j] = S[j], S[i]
        stream_key.append(S[(S[i] + S[j]) % bits])
        cipher_text.append(message[k] ^ stream_key[k])
    return cipher_text


def decrypt(message, key):
    i = 0
    j = 0
    S = key_schedling(key)
    stream_key = []
    plain_text = []

    for k in range(len(message)):
        i = (i + 1) % bits
        j = (j + S[i]) % bits
        S[i], S[j] = S[j], S[i]
        stream_key.append(S[(S[i] + S[j]) % bits])
        plain_text.append(message[k] ^ stream_key[k])
    return plain_text


message = []
key = []

# random으로 10글자 메시지 생성
for i in range(10):
    message.append(random.randrange(0, bits))

# key는 random으로 4글자 생성
for i in range(4):
    key.append(random.randrange(0, bits))

print("message:", message)
print("key:", key)

# 암호화
cipher_text = encrypt(message, key)
print("ciphertext:", cipher_text)

# 복호화
original_text = decrypt(cipher_text, key)
print("decrypted:", original_text)
