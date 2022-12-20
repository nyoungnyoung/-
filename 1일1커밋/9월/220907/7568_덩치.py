# 몸무게 x, 키 y : 덩치 (x, y)
# N명 집단에서 자신보다 큰 덩치의 사람이 k명이면, 자신의 등수는 k+1

import sys
N = int(sys.stdin.readline())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 일단 lst를 돌면서, (x, y)값 비교
# 나보다 큰 애가 등장하면 cnt에 +1, 다른애들이랑 비교 끝나면 cnt+1값을 출력
for i in range(N):
    cnt = 0
    for j in range(N):
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            cnt += 1
    print(cnt+1, end=' ')
