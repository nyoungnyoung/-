# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
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
    # 여기에 코드를 작성하여 함수를 완성합니다.


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    print(caesar('apple', 5))
    # fuuqj
    print(caesar('ssafy', 1))
    # ttbgz
    print(caesar('Python', 10))
    # Zidryx
