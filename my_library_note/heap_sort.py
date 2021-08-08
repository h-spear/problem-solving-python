import heapq


def min_heap_sort(A):
    result = []

    # list를 min heap으로 변환 : O(N)
    heapq.heapify(A)

    for _ in range(len(A)):
        result.append(heapq.heappop(A))
    return result


# def max_heap_sort(A):
#     h = []
#     result = []

#     # max heap 만들기 : 원소로 tuple이 들어가면 첫 번째 원소를 우선순위로 힙을 구성
#     for data in A:
#         heapq.heappush(h, (-data, data))

#     for _ in range(len(h)):
#         result.append(heapq.heappop(h)[1])
#     return result


def max_heap_sort(A):
    h = []
    result = []

    for data in A:
        heapq.heappush(h, -data)

    for _ in range(len(h)):
        result.append(-heapq.heappop(h))
    return result


print(min_heap_sort([4, 1, 7, 3, 8, 5]))
print(max_heap_sort([4, 1, 7, 3, 8, 5]))
