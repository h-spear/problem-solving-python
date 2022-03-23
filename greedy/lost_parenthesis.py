# https://www.acmicpc.net/problem/1541

# sol 1
# input_data = input()
#
# first_minus = input_data.find('-')
#
# result = 0
# if first_minus == -1:
#     result += sum(map(int, input_data.split('+')))
# else:
#     section_1 = input_data[:first_minus]
#     if section_1.count('+') == 0:
#         result += int(section_1)
#     else:
#         section_1 = map(int, section_1.split('+'))
#         result += sum(section_1)
#
#     section_2 = map(int, input_data[first_minus+1:].replace('+', '-').split('-'))
#     result -= sum(section_2)
#
# print(result)
#

# sol 2
import sys

input_data = sys.stdin.readline().rstrip().split("-")

partial_sum = []
for x in input_data:
    item = sum(map(int, x.split("+")))
    partial_sum.append(item)

result = partial_sum[0]
for psum in partial_sum[1:]:
    result -= psum

print(result)
