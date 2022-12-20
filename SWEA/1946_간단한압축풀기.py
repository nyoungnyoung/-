# 원본 문서는 너비가 10인 여러 줄의 문자열로 이루어져 있다.
# 문자열은 마지막 줄을 제외하고 빈 공간 없이 알파벳으로 채워져 있고 마지막 줄은 왼쪽부터 채워져 있다.
# 이 문서를 압축한 문서는 알파벳과 그 알파벳의 연속된 개수로 이루어진 쌍들이 나열되어 있다. (예 : A 5    AAAAA)
# 압축된 문서를 입력 받아 원본 문서를 만드는 프로그램을 작성하시오.

import sys

sys.stdin = open('1946_input.txt','r')
# sys.stdout = open('1946_output.txt','w')

T = int(input())  
for t in range(1,T+1):
    N = int(input())
    tnc = 0
    print(f'#{t}')
    for i in range(N):
        C, K = input().split() # 이렇게 적으면 알아서 C와 K에 입력됨
        K = int(K)
        for j in range(K):
            print(C, end = "")      # print(C)라고만 하면 줄바꿈이 됨
            tnc += 1
            if tnc == 10:
                print()             # 얘 자체가 줄바꿈을 포함하고 있음
                tnc = 0

    print()