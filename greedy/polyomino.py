# https://www.acmicpc.net/problem/1343

import re

string = input()

string = re.sub("XXXX", "AAAA", string)
string = re.sub("XX", "BB", string)

if "X" in string:
    print(-1)
else:
    print(string)
