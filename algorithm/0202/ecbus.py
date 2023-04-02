import sys
sys.stdin = open('ecbus_input.txt')

t = int(input())

for tc in range(1, t + 1):
    k, n, m = map(int, input().split())
    bus = list(map(int, input().split()))
    stations = [0] * (n+1)
    start = 0
    i = 0
    count = 0
    for idx in bus:
        stations[idx] = 1
    while True:
        # if start >= 13:
        #     print(start, i , start +k +i)
        if stations[start + k - i] == 1:
            count += 1
            start += k - i
            i = 0
        else:
            i += 1
        if start + k -i >=n:
            print(f'#{tc} {count}')
            break
        if k == i:
            print(f'#{tc} 0')
            break
        