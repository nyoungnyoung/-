# 농부 : 썩은 과일 몇 개 들어있는 과일봉지
# 과일봉지 입력 받아 썩은 과일 조각을 모두 신선한 것으로 교체 후 리스트 형식으로 출력하는 함수 만들기
# ex) apple, rottenBanana, apple, Rottenorange, orange
# -> ['apple', 'banana', 'apple', orange', 'orange']
# 리스트가 비어있는 경우 빈 리스트 반환
# 반환된 리스트의 요소는 모두 소문자 

fruit = ((input().lower()).replace('rotten', '')).split(',')
print(fruit)