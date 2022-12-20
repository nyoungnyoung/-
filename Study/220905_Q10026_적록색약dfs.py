from collections import deque
import sys

def dfs(x, y):
    # 상/하/좌/우 델타 선언
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    stack = deque([(x, y)])
    visited[x][y] = 1
    while stack:                # 스택이 빌 때까지 반복
        x, y = stack.pop()
        for d in range(4):      # 4방향 델타 탐색
            nx = x + dx[d]
            ny = y + dy[d]
            # (nx, ny)가 arr안에 있고, (x, y) 랑 같은 색이고, 방문한적 없으면 -> 방문처리 & 스택에 넣기
            if 0 <= nx < N and 0 <= ny < N and arr[x][y] == arr[nx][ny] and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                stack.append((nx, ny))

N = int(sys.stdin.readline())
arr = [list(sys.stdin.readline().strip()) for _ in range(N)]
cnt, cnt_x = 0, 0      # 적록색약이 아닌 사람이 봤을 때 / 적록색약인 사람이 봤을 때
# 적록색약이 아닌 사람이 봤을 때
visited = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:      # 방문한적 없으면 같은 색 애들 dfs 탐색하기!!
            dfs(i, j)
            cnt += 1

# 적록색약인 사람이 봤을 때(R / G 구분 못함 -> 하나로 통일시켜서 dfs 탐색)
visited = [[0] * N for _ in range(N)]   # 방문처리하는 arr 초기화
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            dfs(i, j)
            cnt_x += 1

print(cnt, cnt_x)
