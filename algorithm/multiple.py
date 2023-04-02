# 1.  두 수를 입력받는다.
# 2. 수를 곱한다.
    # 2-1. (2)에 10을 나눠서 나머지와 곱해준다.
    # 2-2. (2)의 중간 숫자와 마지막 숫자를 곱한다.


first_num, second_num = map(int, input().split())

last = second_num % 10
mid = int(second_num / 10) % 10
first = mid % 10
result = ((first_num * last) + (first_num * mid) + (first_num * first))
print(first_num * last)
print(first_num * mid)
print(first_num * first)
print(result)

print(mid)