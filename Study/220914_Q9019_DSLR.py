# 델타 대신 DSLR로 bfs 수행
# n = d1d2d3d4
# D : 2n % 10000
# S : n - 1 (if n == 0 -> n = 9999)
# L : (n % 1000) * 10 + (n // 1000) : d2d3d40 + d1
# R : (n % 10) * 1000 + (n // 10) : d4000 + d1d2d3
# A -> B 바꾸는 최소한의 명령어

from collections import deque
import sys

# dslr함수 작성(처음 숫자 n / 델타 대신 사용할 d)
def dslr(n, d):
    if d == 'D':
        return (n * 2) % 10000
    elif d == 'S':
        # if n - 1 == -1:
        #     return 9999
        # else:
        #     return (n - 1)
        return (n - 1) % 10000
    elif d == 'L':
        return (n % 1000) * 10 + (n // 1000)
    elif d == 'R':       # d == 'R' 일때
        return (n % 10) * 1000 + (n // 10)

def bfs(a, b):
    queue = deque([(a, '')])          # 시작하는 숫자 & 명령어 저장할 빈문자열 큐에 넣기
    visited[a] = 1                    # 시작하는 숫자 방문처리
    while queue:                      # 큐가 빌때까지 반복
        x, y = queue.popleft()        # x, y를 큐에서 꺼내오기
        # x가 b와 같아지면 탐색 종료
        if x == b:
            return y
        # x에 dslr함수 사용해서 DSLR 하나씩 적용해보기
        for d in 'DSLR':
            nx = dslr(x, d)
            # nx를 방문한적 없으면 방문처리 후 (nx, y+d) 큐에 넣기
            if visited[nx] == 0:
                visited[nx] = 1
                queue.append((nx, y+d))


T = int(sys.stdin.readline())
for tc in range(T):
    A, B = map(int, sys.stdin.readline().split())
    visited = [0] * 10000
    print(bfs(A, B))