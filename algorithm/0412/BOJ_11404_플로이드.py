n = int(input())
m = int(input())
INF = 1e9
arr = [[INF] * (n + 1) for _ in range(n + 1)]


for i in range(m):
    a, b, c = map(int, input().split())
    arr[a][b] = c
    