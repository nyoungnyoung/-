# word를 양의정수 n만큼 밀어 완성된 시저 암호를 반환하는
# 함수 caesar를 완성하시오
# 대문자는 대문자로, 소문자는소문자로 암호화하기
# islower(), isupper()로 대/소문자 여부 확인가능

# ord(word)+n이 마지막 대/소문자의 10진수 표현을 넘지 않는
# 경우에는 그냥 return, 넘는 경우에는 26을 뺀 수를 return

def caesar(word, n):
    new_word = ''           # 시저암호 담을 변수 설정
    for i in word:          # 반복문 돌리면서 word의 인덱스마다 시행
        if i.islower() == True:     # i가 소문자면 마지막 ord 122
            if ord(i) + n <= 122:
                new_word += (chr(ord(i) + n))
            else:
                new_word += (chr(ord(i) + n - 26))
        if i.isupper() == True:     # i가 대문자면 마지막 ord 90
            if ord(i) + n <= 90:
                new_word += (chr(ord(i) + n))
            else:
                new_word += (chr(ord(i) + n - 26))
    return new_word


# print(caesar('abcd', 3))
# print(caesar('xyz', 3))
# print(caesar('ABCD', 3))
# print(caesar('XYZ', 3))
# print(caesar('AbcD', 3))
