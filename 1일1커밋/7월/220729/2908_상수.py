# 두 수 A, B (같지 않은 세자리 수, 0은 포함x)
# A , B를 거꾸로 읽는 상수가 두 수의 크기 비교해서 출력

A, B = map(int, (input()[::-1].split()))
if A > B:
    print(A)
elif A < B:
    print(B)