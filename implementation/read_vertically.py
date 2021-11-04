# https://www.acmicpc.net/problem/10798

board = [[""] * 15 for _ in range(15)]
for i in range(5):
    input_data = list(input())
    for j in range(len(input_data)):
        board[i][j] = input_data[j]

for j in range(15):
    for i in range(5):
        print(board[i][j], end="")
