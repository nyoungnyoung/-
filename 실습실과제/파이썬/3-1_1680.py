# 농부 : 썩은 과일이 들어있는 과일봉지
# 썩은 과일 조각을 신선한 것으로 교체하는 코드 작성 후 리스트로 출력
# apple,rottenBanana, RoTTenorange, orange
# ['abble', 'banana', 'orange', 'orange']
# 리스트가 빈 경우 빈 리스트 반환
# 리스트 요소는 모두 소문자여야 함

# for문 없이
# fruit = ((input().lower()).replace('rotten', '')).split(',')
# print(fruit)

# for문 사용
new = []
fruits = input().split(',')
for i in fruits:
    new.append((i.lower()).replace('rotten', ''))
print(new)
