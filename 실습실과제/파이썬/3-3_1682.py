infos = [{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}]
sum_value = 0
for i in infos:
    sum_value += i['age']
print(sum_value)

# Dictionary로 이루어진 list를 전달받아 모든 dictionary의 'age'key에 해당하는 value의 합을 구하기
