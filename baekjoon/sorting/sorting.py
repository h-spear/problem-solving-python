array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
print(array)


def selection_sort(A):
    n = len(A)
    for i in range(n - 1):
        least = i
        for j in range(i + 1, n):
            if A[least] > A[j]:
                least = j
        A[i], A[least] = A[least], A[i]


def insertion_sort(A):
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key


def bubble_sort(A):
    n = len(A)
    for i in range(n - 1, 0, -1):
        bChanged = False
        for j in range(i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                bChanged = True

        if not bChanged:
            break


bubble_sort(array)
print(array)
