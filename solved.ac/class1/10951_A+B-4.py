# 입력 : 여러 개의 테스트 케이스
# 각 테스트 케이스는 한 줄로 이루어져 있음
# 각 테스트 케이스마다 A + B 출력

while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break
    