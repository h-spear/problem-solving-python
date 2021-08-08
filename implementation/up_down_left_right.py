n = int(input())
direction = input().split()

pos_x = 1
pos_y = 1

for cmd in direction:
    if cmd == "R" and pos_y < n:
        pos_y += 1
    elif cmd == "L" and pos_y > 1:
        pos_y -= 1
    elif cmd == "U" and pos_x > 1:
        pos_x -= 1
    elif cmd == "D" and pos_x < n:
        pos_x += 1

print(pos_x, pos_y)
