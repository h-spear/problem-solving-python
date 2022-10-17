def solution(polynomial):
    a = 0
    b = 0
    operand = polynomial.split("+")
    for o in operand:
        o = o.replace(" ", "")
        if "x" in o:
            temp = o.replace("x", "")
            if not temp:
                temp = 1
            a += int(temp)
        else:
            b += int(o)

    if b:
        if a == 1:
            return "x + " + str(b)
        elif a == 0:
            return str(b)
        else:
            return str(a) + "x + " + str(b)
    else:
        if a == 1:
            return "x"
        else:
            return str(a) + "x"
