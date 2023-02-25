# https://www.acmicpc.net/problem/1543

import re

string = input()
pattern = input()

print(re.sub(pattern, "!", string).count("!"))
