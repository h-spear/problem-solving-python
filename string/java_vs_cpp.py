# https://www.acmicpc.net/problem/3613
# is_cpp, is_java 조건이 생각보다 많으므로 잘 처리해줘야 함

import re

variable_name = input()


def is_cpp(string):
    if "__" in string:
        return False
    if string[0] == "_" or string[-1] == "_":
        return False
    return "_" in string and string == string.lower()


def is_java(string):
    if "_" in string:
        return False
    if string[0] != string[0].lower():
        return False
    return True


if is_cpp(variable_name):
    words = variable_name.split("_")
    for i, word in enumerate(words):
        if i == 0:
            print(word, end="")
        else:
            print(word.title(), end="")
elif is_java(variable_name):
    variable_name = re.sub("(?=[A-Z])", "_", variable_name)
    print(variable_name.lower())
else:
    print("Error!")
