n = int(input())
components = [0] * 1000001

input_data = list(map(int, input().split()))
for i in input_data:
    components[i] = 1

m = int(input())
demands = list(map(int, input().split()))


def findComponent(index):
    if components[index] == 1:
        return 'yes'
    else:
        return 'no'


for item in demands:
    print(findComponent(item), end=" ")
