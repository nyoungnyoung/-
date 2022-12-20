# 적록색약 : 빨강 초록 구분 못함
# N * N 각 칸이 R, G, B로 칠해져있음
# 같은 색상이 인접해 있는 경우 하나의 구역

from collections import deque
import sys

def bfs(x, y):              # bfs 함수 -> 같은 구역 내 애들 방문처리 됨
    # 상/하/좌/우 델타 선언
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque([(x, y)])   # 첫 시작점 큐에 넣기
    visited[x][y] = 1       # 시작점 방문처리
    while queue:            # 큐가 빌때까지 반복하기
        x, y = queue.popleft()      # x, y를 큐에서 꺼내오기
        for d in range(4):          # 4방향 델타 탐색
            nx = x + dx[d]
            ny = y + dy[d]
            # (nx, ny)가 arr안에 있고, (x, y) 랑 같은 색이고, 방문한적 없으면(visited[nx][ny] == 0) -> 방문체크 후 큐에 넣기
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == arr[x][y] and not visited[nx][ny]:
                visited[nx][ny] = 1
                queue.append((nx, ny))


N = int(sys.stdin.readline())
arr = [list(sys.stdin.readline().strip()) for _ in range(N)]
cnt, cnt_x = 0, 0   # 적록색약이 아닌 사람이 봤을 때 / 적록색약인 사람이 봤을 때
# 적록색약 아닌경우
visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:       # 방문한적 없으면 같은 색 애들 bfs 탐색하기!
            bfs(i, j)
            cnt += 1

# 적록색약인 경우(R랑 G 구분 못함 -> 둘중에 하나로 통일시켜서 bfs 탐색)
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'
visited =[[0]*N for _ in range(N)]      # 방문처리하는 함수 초기화
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            cnt_x += 1

print(cnt, cnt_x)




