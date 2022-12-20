my_dict = {'age' : 17, 'score' : 20, 'height' : 180}    # dictionary는 넣은 순서대로 출력됨(ordered)
my_dict['name'] = '홍길동'

arr = [1,2,3,4]
for el in arr:
    print(el)           # 이런 방법으로 arr이 가지고 있는 모든 요소에 접근할 수 있음

print(my_dict)
print(my_dict.keys())   # 리스트 형태로 my_dict가 가지고 있는 key 전부 출력 가능
print(my_dict.items())  # 리스트 안에 튜플('key',value)이 있는 형태로 출력 가능

# dictionary의 모든 요소에 접근하기
for el in my_dict:
    print(el)           # 키값만 출력 가능

for el in my_dict:
    print(my_dict[el])  # value값만 출력 나으

for item in my_dict.items():    # 튜플 형태로 ('key', value) 출력
    print(item)

# (k, v)
for key, value in my_dict.items():
    print(f'{key} : {value}')

# 특정 요소에 접근할 때 - get 함수 이용
print(my_dict.get('name'))      # name의 value값 출력
print(my_dict.get('namel'))     # None 출력

# 특정 요소에 접근할 때 - ['key'] 활용
print(my_dict['name'])
# print(my_dict['namel'])         # key에러 발생, get함수 쓰는게 더 좋음!

# 형변환 : 1 -> 1.0처럼 자료 손실이 일어나지 않을 경우는 암시적 변환 가능
# 1.0 -> 1 변환이 되지 않음(소수점이라는 자료가 사라지는 것이기 때문)
print(2.0 + 1)  # 1이 1.0으로 변환되고 계산됨! 

# 암시적 형변환 : 사용자가 의도하지 않고, 파이썬 내부적으로 자료형을 변환하는 경우(bool/int와 float)
# 명시적 형변환 : 자료 손실이 일어나는 경우에도 변환 가능
# ex) str, float -> int

# p.132 컨테이너 형 변환

msg = 'Hello'
list_msg = list(msg)
print(list_msg)