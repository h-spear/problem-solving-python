n = int(input())
components = list(map(int, input().split()))

m = int(input())
demands = list(map(int, input().split()))

components.sort()

# binary_search


def findComponent(item, left, right):
    if left > right:
        return "no"

    mid = (left + right) // 2
    if components[mid] == item:
        return "yes"
    elif components[mid] > item:
        return findComponent(item, left, mid - 1)
    else:
        return findComponent(item, mid + 1, right)


for item in demands:
    print(findComponent(item, 0, len(components) - 1), end=" ")
