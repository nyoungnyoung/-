# 알파벳 소문자로만 이루어진 단어 S
# 각 알파벳이 단어에 몇개 포함되어 있는지 구하기
# 아스키코드 이용하면 될듯! ord(문자) = 아스키숫자

S = input()
alpha = [0] * 26                # 알파벳 a ~ z : 26개
for s in S:
    alpha[ord(s) - 97] += 1     # ord('a') = 97
print(*alpha)    

# 리스트 출력 시 반복문(for문) 사용하는 방법도 가능
# for i in alpha:
    # print(i, end=" ")
