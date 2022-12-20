from collections import deque


# bfs + 다익스트라
def bfs(i, j):         # 출발지점 (i, j)
    # 상 / 하 / 좌 / 우 델타
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque([(i, j)])         # 출발지점 큐에 넣어주기
    time[i][j] = graph[i][j]
    while queue:
        x, y = queue.popleft()          # x, y 좌표 큐에서 꺼내오기

        # 델타탐색 시작
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N:     # (nx, ny)가 범위 내에 있으면
                # (nx, ny)좌표의 시간이 (x, y)좌표의 시간에 (nx, ny)에서 걸리는 시간을 더한 값보다 크면
                if time[nx][ny] > time[x][y] + graph[nx][ny]:
                    time[nx][ny] = time[x][y] + graph[nx][ny]       # 더 작은 값으로 업데이트
                    queue.append((nx, ny))                          # 큐에 (nx, ny) 추가
    return time[-1][-1]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input())) for _ in range(N)]
    time = [[0xffff] * N for _ in range(N)]
    print(f'#{tc} {bfs(0, 0)}')
