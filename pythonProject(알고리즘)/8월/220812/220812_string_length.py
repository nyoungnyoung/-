# C언어에서 사용하는 strlen()함수의 동작을 python에서 구현해보자
# C언어에서는 문자열이 존재하지 않고 '문자배열'을 사용한다.
# 문자열이 끝남을 표시하기 위해서 'Null'문자를 문자열 배열 마지막에 넣어줌
# strlen() : 배열에 들어있는 널문자를 만나기 전까지의 문자 개수를 반환

string = ['a', 'b', 'c', 'd', '\0']

def strlen(string):
    length = 0
    for char in string:
        if char != '\0':
            length += 1
        else:
            break
    return length

print(strlen(string))