# 자카드 유사도 : 두 집합의 교집합 크기 / 두 집합의 합집합 크기
# 집합 A, B가 모두 공집합일 경우는 자카드 유사도 1로 정의
# 문자열은 두글자씩 끊어서 다중 집합의 원소로 만듬
# 영문자로 된 글자 쌍만 유효, 기타 공백, 숫자, 특수문자가 들어있으면 버림
# 대문자/소문자 구분x


def solution(str1, str2):
    answer = 0
    str1, str2 = str1.lower(), str2.lower()
    A, B = [], []
    # 두 글자씩 끊어 다중집합의 원소로 만들기
    for i in range(len(str1)-1):
        if (str1[i] + str1[i+1]).isalpha():
            A.append(str1[i] + str1[i+1])
    for j in range(len(str2)-1):
        if (str2[j] + str2[j+1]).isalpha():
            B.append(str2[j] + str2[j+1])
    print(A)
    print(B)

    # return answer


solution('FRANCE', 'french')
