# 델타 대신 (+1, -1, *2, -10)으로 bfs수행
from collections import deque

# bfs함수
def bfs(a, b):      # a : 시작하는 숫자 / b : 목표숫자
    queue = deque([(a, 0)])   # 시작하는 숫자 & 연산 횟수 큐에 넣어주기
    visited[a] = 1          # 시작하는 숫자 방문처리
    while queue:            # 큐가 빌 때까지 반복
        x, y = queue.popleft()  # x, y를 큐에서 꺼내오기
        # x가 b와 같아지면 탐색 종료(y 리턴)
        if x == b:
            return y
        # x에다가 연산 하나씩 적용해보기!(연산 적용한 결과가 범위 내에 있고, 방문한적 없으면 방문처리&큐에 넣기)
        if 0 < x + 1 <= 1000000 and not visited.get(x+1, 0):
            visited[x+1] = 1
            queue.append((x+1, y+1))
        if 0 < x - 1 <= 1000000 and not visited.get(x-1, 0):
            visited[x-1] = 1
            queue.append((x-1, y+1))
        if 0 < x * 2 <= 1000000 and not visited.get(x*2, 0):
            visited[x*2] = 1
            queue.append((x*2, y+1))
        if 0 < x - 10 <= 1000000 and not visited.get(x-10, 0):
            visited[x-10] = 1
            queue.append((x-10, y+1))



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    visited = {}
    # visited = [0] * 1000001
    # 너무 비효율적인것 같아서 딕셔너리로 바꿈
    print(f'#{tc} {bfs(N, M)}')
