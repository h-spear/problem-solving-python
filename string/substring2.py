def substring(string, pattern):
    ls = len(string)
    lp = len(pattern)

    j = 0
    for i in range(ls):
        if string[i] == pattern[j]:
            j += 1

        if j == lp:
            return "Yes"
    return "No"


while 1:
    try:
        s, t = input().split()
        print(substring(t, s))
    except:
        break
