
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    card = list(map(int, input().rstrip()))
    arr = [0] * 10
    for i in card:
        arr[i] += 1
    cnt = 0
    for j in range(10):
        if arr[j] // 3:
            cnt += arr[j] // 3
            arr[j] -= arr[j] // 3 * 3
        if j >= 2:
            if arr[j] and arr[j - 1] and arr[j - 2]:
                arr[j] -= 1
                cnt += 1
    if cnt == 2:
        print(True)
    else:
        print(False)


