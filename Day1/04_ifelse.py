# is_egg_exist = True
# if 조건문:
#    A : 조건문이 참일때 실행하는 문장
# else: 조건문이 거짓일때 실행하는 문장
# 우유 한병 사오는데 달걀이 있으면 6개 사와

# if is_egg_exist:
#     print('우유 6병 사오기')
# else:
#     print('우유 한 병 사오기')


# dust라는 변수에 값을 입력받아서 30미만이라면 '날씨가 좋네요!'출력
# 30 이상이라면 '마스크를 쓰고 외출하세요' 출력

# dust = int(input())
# if dust < 30:
#     print('날씨가 좋네요!')
# else:
#     print('마스크를 쓰고 외출하세요')

dust = int(input())
if dust > 150:
    print('매우나쁨')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')