import sys
input = sys.stdin.readline

boys = []
girls = []
cnt = 0
N, K = map(int, input().split())
for i in range(N):
    S, Y = map(int, input().split())
    if S == 0:
        girls.append(Y)
    else:
        boys.append(Y)

year_boy = sorted(boys)
year_girl = sorted(girls)

