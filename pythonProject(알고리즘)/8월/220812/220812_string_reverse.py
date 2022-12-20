# 문자열 뒤집기
from audioop import reverse


a = 'Hello world!'
b = a[::-1]
print(b)

# 저거 안쓰고 뒤집어보자는게 목표
# 반 짤라서 첫번째와 마지막요소, 두번재와 마지막에서 두번째요소 이런식으로 바꾸자는거!
# for문 이용해서 뒤집어주기(앞쪽부터 순회하면서, 가장뒤에 있는 문자와 자리교환)
# 중간지점이 되면 멈추기

s = 'Reverse this string'
for i in range(len(s)//2):
    s.replace(s[i], s[-1-i])
    s.replace(s[-1-i], s[i])
print(s) 

# 교수님코드
lst = list(s)
M = len(lst)
for i in range(len(M/2)):
    # 0번째 요소와 M-1 / 1번 요소와 M-2 / 2번 요소와 M-3
    # i번째 요소와 M-1-i번요소 교환
    lst[i], lst[M-1-i] = lst[M-1-i], lst[i]
    # 파이썬에서는 이렇게 교환하는데 다른 언어에서는 이 방법 안됨...! 아래처러
    # tmp = lst[i]
    # lst[i] = lst[m-1-i]
    # lst[M-1-i] = tmp
    print(''.join(lst))