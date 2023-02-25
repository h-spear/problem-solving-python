# https://www.acmicpc.net/problem/10988

string = input()
print(sum([string == string[::-1]]))
