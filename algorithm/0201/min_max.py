import sys
sys.stdin = open('sample_input.txt')


t = int(input())

for i in range(1, t + 1):
    n = input()
    numbers = input().split()
    min = int(numbers[0])
    max = int(numbers[0])
    for num in numbers:
        if int(num) < min:
            min = int(num)
        if int(num) > max:
            max = int(num)
    print(f'#{i} {max - min}')

