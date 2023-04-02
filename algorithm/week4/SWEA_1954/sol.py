import sys
sys.stdin = open('input.txt')

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    mat = [[0] * N for _ in range(N)]
    x, y = 0, 0
    dh = 0
    mat[y][x] = 1
    for i in range(1, (N * N) + 1):
        mat[y][x] = i
        if 0 <= y + dy[dh] < N and 0 <= x + dx[dh] < N and mat[y + dy[dh]][x + dx[dh]] == 0:
            y = y + dy[dh]
            x = x + dx[dh]
        else:
            if dh == 3:
                dh = 0
            else:
                dh += 1
            y = y + dy[dh]
            x = x + dx[dh]
    print(f'#{tc}')
    for row in mat:
        print(*row)







