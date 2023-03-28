import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    for i in range(1, N):
        board[0][i] += board[0][i - 1]
        board[i][0] += board[i - 1][0]
    for y in range(1, N):
        for x in range(1, N):
            if board[y - 1][x] < board[y][x - 1]:
                board[y][x] += board[y - 1][x]
            else:
                board[y][x] += board[y][x - 1]
    print(f'#{tc} {board[N - 1][N - 1]}')

