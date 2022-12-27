# itoa(int->str) / atoi(str->int)
# 파이썬은 int() / str() 함수 사용하면 되지만, 한번 만들어서 사용해보자는거!
# atoi : 각 숫자형문자의 아스키코드 번호에서 '0'의 아스키 코드번호 빼기
# 파이썬에서 문자의 아스키코드를 얻는 법 : ord()함수 사용
# 특정 아스키코드에 해당하는 문자 얻는 법 : chr()함수 사용
# ex) 문자열 1을 숫자 1로 바꾸고 싶다면? 문자열 1의 아스키코드(49) 확인, 
# 여기서 48(0의 아스키코드) 빼주면 1이 됨

def atoi(data):
    # data '123', '12345'
    result = 0
    for i in range(len(data)):
        # 현재인덱스의 문자를 숫자로 변경
        num = ord(data[i])- ord('0')
        result = result*10 + num
    return result

result = atoi('12345')
print(result, type(result))

# 12345 >>> '12345'
# 1 + ord('0') 이용
# 숫자를 문자열로 받는거부터가 문제임..!
def itoa(num):
    # 숫자를 10으로 나누고, 나머지를 문자열로 변경해서 저장
    # 몫은 다시 10으로 나눠서 나머지를 문자열로 변경해서 저장
    # 몫이 0이 될때까지 계속 반복
    result = ''
    while num > 0:
        # 몫이 필요한게 아니라, 나머지가 필요함!
        remain = num % 10
        # remain + ord('0') : remain의 아스키코드 얻을 수 있음
        result = chr(remain + ord('0')) + result
        num = num // 10
    return result

result2 = itoa(12345)
print(result2, type(result2))
# result = itoa(-1234)
# print(result, type(itoa))



# 지나쓰 코드
# def itoa(i):
#     s=''
#     num=str(i)
#     for i in range(len(num)):
#         s+=chr(int(num[i])+48)
#     return s

# print(itoa(123)+itoa(123))


# def itoa2(i):
#     s=''
#     while i/10>0:
#         s=chr(i%10+48)+s
#         i=i//10
#     return s

# print(itoa2(456)+itoa2(456))