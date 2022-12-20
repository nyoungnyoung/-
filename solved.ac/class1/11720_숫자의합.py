# 첫째줄에 숫자의 개수 N이 주어진다.
# 둘째줄에 숫자 N개가 공백없이 주어진다.
# 숫자 N개의 합을 출력한다.

N = int(input())
number = input()    # number 는 문자형, 인덱스 사용가능
sum_number = 0      # 각 숫자들이 차곡차곡 더해질 변수 선언

for i in range(N):  # 0 ~ N-1 반복
    sum_number += int(number[i])       # number의 i번째 인덱스를 정수화하여 sum_number에 더해라

print(sum_number)
