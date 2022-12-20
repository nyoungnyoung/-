'''
N명의 신입사원, 입사당시 어학점수에 따라 3개의 분반(A, B, C반)으로 나눔
-> C반 T1 B반 T2 A반 으로 배정
각 반의 인원은 최소 인원(K_min)과 최대 인원(K_max) 사이에 존재해야 함!
N명의 신입사원은 반드시 하나의 분반에 배정이 되어야 한다.
N : 총 인원 수  / K_min, K_max : 한 분반에 들어갈 수 잇는 최소, 최대 인원
lst : 각 사원들의 어학점수
result = min(인원이 가장 많은 분반 인원수 - 인원이 가장 적은 분반 인원수)
조건을 만족하는 반 배정이 불가능할 경우 -1 출력
'''
from itertools import combinations


def lan_class(data):
    data.sort()
    T_lst = list(combinations(set(data), 2))
    result = 1001
    for idx in T_lst:
        T1, T2 = idx[0], idx[1]
        A, B, C = 0, 0, 0
        for i in data:
            # i가 T1보다 작을 때 A반 인원수 +1, T1보다 크거나 같고 T2보다 작을때 B반 인원수 +1, T2보다 크거나 같을때 C반 인원수 +1
            if i < T1:
                A += 1
            if T1 <= i < T2:
                B += 1
            if i >= T2:
                C += 1
        # for문 다 돌고나면 A, B, C에 분배 완료됨
        # 최소인원과 최대인원 조건 맞을때만 최대/최소 인원 수 차이를 result랑 비교해가면서 min값 찾기
        if K_min <= A <= K_max and K_min <= B <= K_max and K_min <= C <= K_max:
            tmp = max(A, B, C) - min(A, B, C)
            if result >= tmp:
                result = tmp
    if result == 1001:
        return -1
    else:
        return result



T = int(input())
for tc in range(1, T + 1):
    N, K_min, K_max = map(int, input().split())
    lst = list(map(int, input().split()))
    min_num = lan_class(lst)
    print(f'#{tc} {min_num}')