# N개의 정수 A[1], A[2], …, A[N]이 주어질 때
# 이 안에 X라는 정수가 존재하는지 알아내기

import sys
N = int(sys.stdin.readline())
lst = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
m_lst = list(map(int, sys.stdin.readline().split()))
for m in m_lst:
    if m in lst:
        print(1)
    else:
        print(0)
