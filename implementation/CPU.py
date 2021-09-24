# https://www.acmicpc.net/problem/16506

opcode = {
    "ADD": "0000",
    "SUB": "0001",
    "MOV": "0010",
    "AND": "0011",
    "OR": "0100",
    "NOT": "0101",
    "MULT": "0110",
    "LSFTL": "0111",
    "LSFTR": "1000",
    "ASFTR": "1001",
    "RL": "1010",
    "RR": "1011",
}


def binary(string, len):
    trans = ["0"] * len
    num = int(string)
    i = len - 1
    while num:
        trans[i] = str(num % 2)
        num //= 2
        i -= 1
    return "".join(trans)


for _ in range(int(input())):
    cmd = input().split()
    code = ""

    op = cmd[0].replace("C", "")
    code += opcode[op]
    if cmd[0][-1] == "C":
        code += "1"
    else:
        code += "0"
    code += "0"
    code += binary(cmd[1], 3)

    if op == "MOV" or op == "NOT":
        code += "000"
    else:
        code += binary(cmd[2], 3)

    if cmd[0][-1] == "C":
        code += binary(cmd[3], 4)
    else:
        code += binary(cmd[3], 3)
        code += "0"

    print(code)
