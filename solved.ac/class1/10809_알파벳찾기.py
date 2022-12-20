# S : 알파벳 소문자로 이루어진 단어
# a가 처음등장하는 위치/b가 처음 등장하는 위치/....z가 처음 등장하는 위치를 공백 구분하여 출력
# 알파벳이 단어에 포함되어 있지 않다면 -1 출력
# 위치는 인덱스 기준, 알파벳 개수는 총 26개

S = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in range(26):  # 0~25까지 반복
    print(S.find(f'{alphabet[i]}'), end=" ")  # S.find('')
