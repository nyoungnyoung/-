# year : 400의 배수이면 윤년
# year : 4의 배수 & 100의 배수가 아니면 윤년

year = int(input())
if year % 400 == 0:
    print(True)
elif year % 4 == 0:
    if year % 100 != 0:
        print(True)
    else:
        print(False)
else:
    print(False)
