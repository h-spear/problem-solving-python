# https://www.acmicpc.net/problem/4659


def check_pwd(pwd):
    for i in ["a", "e", "i", "o", "u"]:
        if i in pwd:
            break
        if i == "u":
            return False

    cnt = 0
    vowel = True
    for x in pwd:
        if x in ["a", "e", "i", "o", "u"]:
            if vowel:
                cnt += 1
            else:
                cnt = 1
                vowel = True
        else:
            if not vowel:
                cnt += 1
            else:
                cnt = 1
                vowel = False
        if cnt == 3:
            return False

    for i in range(len(pwd) - 1):
        if pwd[i] == pwd[i + 1]:
            if pwd[i] == "o":
                continue
            if pwd[i] == "e":
                continue
            return False
    return True


while 1:
    pwd = input()
    if pwd == "end":
        break

    print("<{}> is".format(pwd), end=" ")
    if check_pwd(pwd):
        print("acceptable.")
    else:
        print("not acceptable.")
