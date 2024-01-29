# https://www.acmicpc.net/problem/20006

import sys

input = lambda: sys.stdin.readline().rstrip()


class Room:
    def __init__(self, level, capacity):
        self.lower = level - 10
        self.upper = level + 10
        self.capacity = capacity
        self.users = []

    def add(self, user):
        if self.lower > user[0] or user[0] > self.upper:
            return False
        if len(self.users) >= self.capacity:
            return False
        self.users.append(user)
        return True


def main():
    p, m = map(int, input().split())
    rooms = []
    for _ in range(p):
        l, n = input().split()
        l = int(l)

        for room in rooms:
            if room.add((l, n)):
                break
        else:
            newRoom = Room(l, m)
            newRoom.add((l, n))
            rooms.append(newRoom)

    sb = []
    for room in rooms:
        room.users.sort(key=lambda x: x[1])
        sb.append("Started!" if (len(room.users) == m) else "Waiting!")
        for user in room.users:
            sb.append(" ".join(map(str, user)))

    print("\n".join(sb))


if __name__ == "__main__":
    main()
