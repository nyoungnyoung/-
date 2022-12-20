# 특수문자 제거 방법
# str.isalnum() 메서드 : 문자가 영숫자문자인 경우 True 반환(특수문자 없음 의미)
# filter(str.isalnum, string) 메서드
# 이렇게 할 필요 없네ㅋㅋ

# 특수문자 문자열 특수문자
# 공백 기준으로 나누어 입력받기(list형태)
# list의 index 0과 -1 삭제
# str.capitalize() 메서드 : 첫번째 문자가 대문자이고 나머지 문자가 소문자인 문자열 얻기
#

s = input().split()
s[0] = ''.join(filter(str.isalnum, s[0]))
s[-1] = ''.join(filter(str.isalnum, s[-1]))
# 리스트 요소 사이에 ' '(공백)을 넣어 문자열로 변환
result = ' '.join(s)
print(f'\'{result.capitalize()}\'')
