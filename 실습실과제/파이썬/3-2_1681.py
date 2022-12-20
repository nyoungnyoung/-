# 문자열을 전달받아 해당 문자열의 정중앙 문자를 출력하기
# 문자열 길이가 짝수일 경우 정중앙 문자 2개 출력


word = input()

if len(word) % 2 == 0:
    # 문자열 슬라이싱 시 [a:b] a부터 b-1까지만 슬라이싱됨!!
    print(word[len(word)//2-1:len(word)//2+1])
else:
    print(word[len(word)//2])
