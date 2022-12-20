# 이 중에서 아무거나 하나 뽑아서 보여주기
# 실행할 때마다 계속 달라진다
# random 함수를 활용

import random

# menu = ['잔치국수', '유니짜장', '깡생수']
# selected = random.choice(menu)
# print(f'오늘의 메뉴는 {selected} 입니다.')

# arr = [1,2,3,4,5,6,7,8,9]
# print(random.sample(arr,3))

# 실습 : 로또 번호 생성기를 작성하세요
# 1~45 정수 중에서 중복되지 않는 6개의 정수를 출력
# 정렬할 수 있을거 같으면 정렬해도 됨

# lotto = []

# for i in range(1,46):
#     lotto.append = i

# print(lotto)

# numbers = range(1,46)
# lucky = sorted(random.sample(numbers,6))
# print(lucky)


print(type(list(range(1,46))))
