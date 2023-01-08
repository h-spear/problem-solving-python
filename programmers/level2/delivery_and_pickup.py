# https://school.programmers.co.kr/learn/courses/30/lessons/150369


def solution(cap, n, deliveries, pickups):
    answer = 0

    while deliveries and deliveries[-1] == 0:
        deliveries.pop()

    while pickups and pickups[-1] == 0:
        pickups.pop()

    while deliveries or pickups:
        delivery_dist = len(deliveries)
        delivery_count = 0
        while deliveries:
            if delivery_count + deliveries[-1] <= cap:
                delivery_count += deliveries.pop()
            else:
                deliveries[-1] -= cap - delivery_count
                break

        pickup_dist = len(pickups)
        pickup_count = 0
        while pickups:
            if pickup_count + pickups[-1] <= cap:
                pickup_count += pickups.pop()
            else:
                pickups[-1] -= cap - pickup_count
                break

        answer += max(delivery_dist, pickup_dist) * 2

    return answer
