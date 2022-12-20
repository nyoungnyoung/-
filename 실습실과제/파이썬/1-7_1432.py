sum_number = 0
s = input('숫자를 입력해주세요 : ')
for i in s:
    sum_number += int(i)
print(sum_number)

# 교수님 코드
# '123' str >>> ['1','2',3'] list >>> 1,2,3 int >>> sum()
# '123' str >>> 123 int >>> 12,3 >>> 1,2 >>> 0,1

# 첫번째 방법
print(sum(map(int,list(input('숫자를 입력해주세요 : ')))))

# 두번째 방법
s = input('숫자를 입력해주세요 : ')
num = int(s)    # 입력받은 문자열을 정수로 변환한 것
result = 0      # 총합을 저장하기 위한 변수
# 10으로 나눈 나머지를 더하고, 몫은 다시 계산 >> 반복 (몫이 0이 될때까지)
while num > 0:
    result += num % 10
    num //= 10 
print(result)