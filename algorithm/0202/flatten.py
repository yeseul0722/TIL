# 테스트 케이스만큼 반복하기
# 덤프 횟수 입력받기
# 상자의 높이값 입력받기
# 덤프 횟수가 반복되는 동안
# for문 돌면서 max와 min 값 구하기
# high - 1 , low + 1 하기
# 변경된 값 형태로 저장하기
# 반복하기
# high - low 값 구하기
# 출력
import sys
sys.stdin = open('flatten_input.txt')

for tc in range(1, 11):
    dump = int(input())
    height = list(map(int, input().split()))
    for _ in range(dump):
        high = height.index(max(height))
        low = height.index(min(height))
        height[high] -= 1
        height[low] += 1
    difference = max(height) - min(height)
    print(f'#{tc}', difference)
                

        
    