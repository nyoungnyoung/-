# 내 코드
A, B = input().split('-')
number = A + B
print(f'{number[:-7]}*******')

# 교수님 코드
# 입력에서 6개 잘라내고, 뒤에 7개 붙이면 됨
# 111111-1234567
# 2345671234567
# num1 = input()
# num2 = input()
# result1 = num1[:6] + '*' * 7
# result2 = num2[:6] + '*' * 7
# print(result1)
# print(result2)