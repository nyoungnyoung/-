# 세 개의 자연수 A, B, C
# A * B * C 결과에 0부터 9까지 각각의 숫자가 몇번씩 쓰였는지 구하시오
# list.count(i) : list 안에 i가 몇 개 있는지 조사하여 개수를 출력

A = int(input())
B = int(input())
C = int(input())
ABC = list(str(A * B * C))

for i in range(10):
    print(ABC.count(str(i)))    # i 는 숫자, 문자형태로 바꿔주어야 리스트 내의 문자와 비교 가능
    i += 1
