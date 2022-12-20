# 여러 개의 소금물을 섞었을 때, 혼합된 소굼물의 농도와 양을 계산
# 소금물의 농도와 양을 입력하고 Done을 입력하면 출력되게 만들기
# 최대 5개의 소금물 입력
# 농도와 양이 소수점 2자리를 넘어갈 경우 반올림하여 2번째 자리까지 나타내기
# 농도 = 소금양 / 소금물양 * 100

salt = 0
water = 0
for i in range(5):
    info = input().split()
    if info[0] == 'Done':
        break
    salt += int(info[0])
    water += int(info[1])
print(round(salt / water * 100, 2), round(water, 2))
