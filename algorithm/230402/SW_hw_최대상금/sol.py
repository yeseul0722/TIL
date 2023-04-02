import sys
sys.stdin = open('input.txt')


def swap(num_list, count):
    global result

    comp = int(''.join(num_list))   # num_list에 있는 리스트 문자열로 합친 후 숫자형으로 변환
    if comp in result[count]:       # result[count](visited라고 생각하면 됌)에 comp가 있으면 return
        return
    else:
        result[count].append(comp)  # 없으면 추가하기

    if count == 0:                  # count가 0이 되면 count만큼 교환이 다 이루어진거니 return
        return

    for i in range(N):
        for j in range(i + 1, N):       # 자신이랑 바뀌지 않게 i + 1 로 범위 설정
            num_list[i], num_list[j] = num_list[j], num_list[i]     # 숫자 바꾸기
            swap(num_list, count - 1)                               # count - 1 하고 재귀 함수 호출
            num_list[i], num_list[j] = num_list[j], num_list[i]     # 함수 호출이 끝나면 다시 원래대로 숫자 돌려놓기



T = int(input())
for C in range(1, T + 1):
    num, cnt = input().split()
    cnt = int(cnt)
    num_list = list(num)    # 문자열 리스트에 저장
    N = len(num_list)
    result = [[] for _ in range(cnt + 1)]       # visited 생성
    swap(num_list, cnt)
    print(f'#{C} {max(result[0])}')             # count = 0 이면 count만큼 숫자를 교환했다는 말
                                                # 즉 result[0] 요소 중 가장 큰 값을 print



'''
#1 321
#2 7732
#3 857147
#4 87664
#5 88832
#6 777770
#7 966354
#8 954311
#9 332211
#10 987645
'''