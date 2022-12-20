# 9개의 서로 다른 자연수가 주어짐
# 이 중 최댓값을 찾고, 그 최댓값이 몇번째 수인지 구해라
# 입력되는 수들을 저장해주는 변수를 하나 만들어서 차곡차곡 쌓아주자
# max함수 사용 : 반복가능한 자료형에만 사용가능(문자열, 리스트 등)

number = []

for i in range(9):               # 9번 반복
    number.append(int(input()))  # 입력된 수를 number에 차곡차곡 쌓아주자

max = max(number)
print(max)                       # number 내에서 가장 큰 수 출력
print(number.index(max) + 1)     # max(number)의 인덱스 출력
