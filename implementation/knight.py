pos = input()

count = 0

# steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
to_x = [1, 1, 2, 2, -1, -1, -2, -2]
to_y = [2, -2, 1, -1, 2, -2, 1, -1]

x = ord(pos[0]) - 96
y = int(pos[1])

for i in range(0, len(to_x)):
    nx = x + to_x[i]
    ny = y + to_y[i]

    if nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8:
        count += 1

print(count)
