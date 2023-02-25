# https://www.acmicpc.net/problem/3568

declaration = input().replace(",", "").replace(";", "").split()
common = declaration[0]
variables = declaration[1:]

for var in variables:
    name = var.replace("*", "").replace("&", "").replace("[]", "")
    var = var.replace(name, "").replace("[]", "!")
    answer = common
    answer += "".join(reversed(var)).replace("!", "[]")
    answer += " "
    answer += name
    answer += ";"
    print(answer)
