# 숫자 + 알파벳 소문자 -> 숫자를 모두 찾아 비내림차순으로 정리
# 숫자 앞에 0이 있는 경우 생략 가능
import sys

N = int(sys.stdin.readline().strip())
lst = []
for _ in range(N):
    word = sys.stdin.readline().strip()
    num = ''
    for i in word:
        # i가 숫자일 때 num에 추가해주기
        if i.isdigit():
            num += i
        # i가 문자일 때
        else:
            # num이 빈 문자열이면 continue
            if num == '':
                continue
            # num이 빈문자열이 아니면 lst에 num 숫자로 변환해서 추가
            else:
                lst.append(int(num))
                num = ''
    # for문 다 돌고 나서 num이 빈문자열이 아닐 경우
    # lst에 num 마저 추가해주기
    if num:
        lst.append(int(num))
for j in sorted(lst):
    print(j)


# 정규표현식 사용방법