#점심 메뉴 3개를 저장하고 출력하는 프로그램 작성
# menu1 = '잔치국수'
# menu2 = '유니짜장'
# menu3 = '깡생수'

# print(menu1)
# print(menu2)
# print(menu3)

menu = ['잔치국수', '유니짜장', '깡생수']
# print(menu[2])

# while문
i=0
while i <=2:
    # 조건이 만족하면 실행할 문장
    # 조건검사를 변경하기 위한 코드
    print(menu[i])
    i += 1
print('while 끝!')

#for문 : 덩어리 데이터를 하나씩 접근 하도록 해 줌
for element in menu:
    print(element)

print('for문 끝!')
