# 시간초과난 코드ㅋㅋ..
# 분산처리 하는 방법이 따로 있다고 해서
# 내일 다시 한번 풀어 보겠습니다!

import sys
T = int(sys.stdin.readline())
for i in range(T):
    a, b = map(int, input().split())
    print(a ** b % 10)
