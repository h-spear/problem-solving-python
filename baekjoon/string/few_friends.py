# https://www.acmicpc.net/problem/16171
# https://www.acmicpc.net/problem/16172

import re

parent = input()
pattern = input()
print(sum([pattern in re.sub("[0-9]", "", parent)]))
