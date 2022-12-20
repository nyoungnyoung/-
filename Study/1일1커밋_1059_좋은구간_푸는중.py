# 좋은 구간 : A < B / A <= x <= B 모든 x가 집합 x에 속하지 않음
# 두 조건을 만족하는 구간 [A, B]를 좋은 구간이라고 함
# 집합의 크기 : L / 집합에 포함된 정수 lst가 주어질 때
# n을 포함하는 좋은 구간의 개수 출력

import sys
L = int(sys.stdin.readline())
S = list(map(int, sys.stdin.readline().split()))
n = int(sys.stdin.readline())
S.sort()
if n not in S:
    for _ in range(2):      # n의 왼쪽 / 오른쪽 구간 비교해야하니까 2번 반복
        while True:
            