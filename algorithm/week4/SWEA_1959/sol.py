import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    result = 0
    if N > M:
        N, M = M, N
        A, B = B, A
    if M > N:
        for i in range(M - N + 1):
            tmp = 0
            for j in range(N):
                tmp += B[i+j] * A[j]
            if result < tmp:
                result = tmp
    print(result)


