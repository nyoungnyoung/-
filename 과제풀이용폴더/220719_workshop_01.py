# 변수-할당연산자
from re import A


x = '과제가 너무 많다..'
print(type(x))
print(id(x))

# 변수-변수연산
i = 5
j = 3
s = '파이썬'
i = i - j
j = -2
print(i * j)
print(i * j / 3)
print('안녕' + s)
s = s * 3
print(s)
s = 'Python'
print(s + ' is fun')

# 변수-변수할당
x = 2
y = 2
print(x, y)
x, y = 1, 2
print(x, y)

# 변수-실습문제
x, y = 10, 20
# 임시 변수 활용
temp = x
x = y
y = temp
print(x, y)
# Pythonic
x, y = y, x
print(x, y)

# 식별자
import keyword
print(keyword.kwlist)

# 사용자입력(input)
# data = input()
# print(data)
# name = input('이름을 입력 해 주세요. : ')
# print(name)
# print(type(name))

# 자료형-불린형
print(type(True))
print(type(False))
print(bool('#'))
print(bool(0))
print(bool(''))
print(bool(1))
print(bool([]))
print(bool(-1))
print(bool([1,2,3]))

# 자료형-수치형-int
a = 3
print(type(a))

a = 2 ** 64
print(a)
print(type(a))

import sys
max_int = sys.maxsize
# sys.maxsize 의 값은 2**63 - 1 => 64비트에서 부호비트를 뺀 63개의 최대치
print(max_int)
super_max = sys.maxsize * sys.maxsize
print(super_max)

binary_number = 0b10
octal_number = 0o10
decimal_number = 10
hexadecimal_number = 0x10
print(f"""2진수 : {binary_number}
8진수 : {octal_number}
10진수 : {decimal_number}
16진수 : {hexadecimal_number}
""")

# 자료형-수치형-float
a = 3.5
print(type(a))

# 여기부터는 주피터노트북에서 실행함