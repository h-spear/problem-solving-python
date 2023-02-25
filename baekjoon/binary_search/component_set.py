n = int(input())
components = set(map(int, input().split()))

m = int(input())
demands = list(map(int, input().split()))


def findComponent(item):
    if item in components:
        return "yes"
    else:
        return "no"


for item in demands:
    print(findComponent(item), end=" ")
