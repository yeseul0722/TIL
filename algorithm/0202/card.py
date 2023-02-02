import sys
sys.stdin = open('card_input.txt')

t = int(input())    #test case 입력받기
for i in range(1, t + 1):   #test case 돌아가는 동안
    num = input()   # 갯수 입력받기
    numbers = input()   # 카드 입력받기
    indexes = [0] * 10  # 카드 번호만큼 빈 리스트 만들기
    max_num = 0     # 최대값 초기값 설정
    mode = 0        # 최빈값 초기값 설정
    for n in numbers:    # 입력받은 카드값을 순회하는 동안
        indexes[int(n)] += 1    # 빈 인덱스의 n번째 요소에 1 더하기
    for idx in range(10):   # 10을 순회하면서
        if indexes[idx] >= mode:    # 인덱스의 idx의 값이 도는 동안 mode값보다 크면
            mode = indexes[idx]     # 최빈값은 인덱스의 idx번째 값
            max_num = idx           # 최대값은 idx
    print(f'#{i}', max_num, mode)




