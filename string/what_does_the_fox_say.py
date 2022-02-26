# https://www.acmicpc.net/problem/9536

for tc in range(int(input())):
    string = list(input().split())
    sounds = set()
    while 1:
        _, *c, sound = input().split()
        if c[0] != "goes":
            break
        sounds.add(sound)

    for sound in string:
        if sound in sounds:
            continue
        print(sound, end=" ")
