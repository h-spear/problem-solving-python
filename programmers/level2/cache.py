# https://programmers.co.kr/learn/courses/30/lessons/17680
# deque maxlen

from collections import deque


def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)

    answer = 0
    cache = deque()
    for city in cities:
        city = city.lower()

        hit = False
        for i, x in enumerate(cache):
            if x == city:
                del cache[i]
                cache.append(city)
                hit = True
                answer += 1
                break
        if not hit:
            if len(cache) >= cacheSize:
                cache.popleft()
            cache.append(city)
            answer += 5

    return answer
