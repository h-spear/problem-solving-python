# https://school.programmers.co.kr/learn/courses/30/lessons/81303


class Node:
    def __init__(self, i):
        self.num = i
        self.up = i - 1
        self.down = i + 1
        self.state = "O"


class Table:
    def __init__(self, n, k):
        self.size = n
        self.k = k
        self.stack = []
        self.table = dict()
        for i in range(n):
            self.table[i] = Node(i)
        self.table[0].up = None
        self.table[n - 1].down = None

    def execute(self, cmd):
        if cmd == "C":
            self.delete()
        elif cmd == "Z":
            self.undo()
        else:
            d, x = cmd.split()
            if d == "U":
                self.up(int(x))
            else:
                self.down(int(x))

    def up(self, x):
        p = self.k
        for i in range(x):
            p = self.table[p].up
        self.k = p

    def down(self, x):
        p = self.k
        for i in range(x):
            p = self.table[p].down
        self.k = p

    def delete(self):
        item = self.table[self.k]
        item.state = "X"
        self.stack.append(item)

        if item.up != None:
            self.table[item.up].down = item.down

        if item.down != None:
            self.table[item.down].up = item.up

        if item.down != None:
            self.k = item.down
        else:
            self.k = item.up

    def undo(self):
        item = self.stack.pop()
        num = item.num
        self.table[num].state = "O"

        if item.up != None:
            self.table[item.up].down = num

        if item.down != None:
            self.table[item.down].up = num

    def get_result(self):
        result = ""
        for i in range(self.size):
            result += self.table[i].state
        return result


def solution(n, k, cmd):
    table = Table(n, k)
    for c in cmd:
        table.execute(c)

    return table.get_result()
