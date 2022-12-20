def dfs(x, y, route):                                               # route 저장해 줄 변수
    global start
    route.append(arr[x][y])                                         # route에다가 현재 위치의 디저트 종류 추가해주기
    if (x, y) == start:                                             # 시작점에 도착하면
        route_lst.append(route)
        return
    # 시계방향 델타 선언
    dx = [1, 1, -1, -1]
    dy = [1, -1, -1, 1]
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and arr[nx][ny] not in route:     # arr[nx][ny]가 범위 안에 있고 방문한 적 없고, 디저트 종류가 route안에 없을때
            visited[nx][ny] = 1                                     # 방문처리
            dfs(nx, ny, route)                                      # nx, ny에서 dfs 돌려보자!
            visited[nx][ny] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    route_lst = []
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            start = (i, j)
            dfs(i, j, [])
    print(route_lst)