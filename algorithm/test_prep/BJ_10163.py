import sys
input = sys.stdin.readline

board = [[0] * 1001 for _ in range(1001)]
N = int(input())

for k in range(1, N + 1):
    x, y, width, height = map(int, input().split())
    for i in range(x, x + width):
        for j in range(y, y + height):
            board[i][j] = k

for k in range(1, N + 1):
    cnt = 0
    for m in board:
        cnt += m.count(k)
    print(cnt)





