A, B = map(int, input().split())
C = int(input())

need = B + C
hour = need // 60
min = need % 60

if need >= 60:
    if A + hour >= 24:
        A -= 24
    A += hour
    print(A, min)
else:
    if A >= 24:
        A-= 24
    print(A, need)

