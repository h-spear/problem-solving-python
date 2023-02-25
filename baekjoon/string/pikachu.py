# https://www.acmicpc.net/problem/14405

import re

string = re.sub("(pi)", "_", input())
string = re.sub("(ka)", "_", string)
string = re.sub("(chu)", "_", string)
string = re.sub("_", "", string)
if string:
    print("NO")
else:
    print("YES")
