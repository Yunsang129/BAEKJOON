board_1 = [] 
board_2 = []
big_board = []
result = []
for _ in range(4):
    board_1.append("WBWBWBWBWB")
    board_1.append("BWBWBWBWBW")
for _ in range(4):
    board_2.append("BWBWBWBWBW")
    board_2.append("WBWBWBWBWB")
b, a= map(int,input().split())
for i in range(b):
    big_board.append(input())

for x in range(b - 7):
    for y in range(a - 7):
        sum_1 = 0
        sum_2 = 0
        for dy in range(8):
            for dx in range(8):
                if board_1[dx][dy] != big_board[x + dx][y + dy]:
                    sum_1 += 1
                if board_2[dx][dy] != big_board[x + dx][y + dy]:
                    sum_2 += 1
        result.append(sum_1)
        result.append(sum_2)
print(min(result))