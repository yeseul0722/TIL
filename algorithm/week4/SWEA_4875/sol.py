import sys
sys.stdin = open('sample_input.txt')

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def search(x, y):
    stack = [(x, y)]
    visited[x][y] = 1
    while stack:
        x, y = stack.pop()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nx < N and 0 <= ny < N and maze[ny][nx] != 1 and visited[nx][ny] != 1:
                if maze[nx][ny] == 3:
                    return 1
                stack.append((nx, ny))
                visited[nx][ny] = 1
            return 0



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = []

    for _ in range(N):
        data = list(map(int, input().rstrip()))
        maze.append(data)

    visited = [[0] * N for __ in range(N)]
    for y in range(N):
        for x in range(N):
            if maze[y][x] == 2:
                startY = y
                startX = x
                visited[y][x] = 1
                break


