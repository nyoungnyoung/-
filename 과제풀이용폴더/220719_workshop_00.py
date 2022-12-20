# 좋아하는 점심메뉴를 이용하여 key는 메뉴, value는 가격인 dictionary를 만들고,
# 점심메뉴의 평균 값을 출력하시오

menu = {'삼계탕' : 14000, '짜장면' : 6000, '해장국' : 8000}
print(int(sum(menu.values())/len(menu)))