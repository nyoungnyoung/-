def bfs(arr, s):
    # 상 / 하 / 좌 / 우 델타
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    queue = [s]          # 큐 만들어주고 시작점 넣어줌
    while queue:                # 큐가 빌때까지 반복
        sr, sc = queue.pop(0)   # 방문하자마자 바로 pop해서 시작지점의 r, c값 튜플에서 받아오기
        visited[sr][sc] = 1     # 시작점 방문처리
        for d in range(4):
            # 시작점의 상하좌우 돌면서 0이 있고 방문하지 않은곳이면 갈 수 있음
            nr, nc = sr + dr[d], sc + dc[d]
            if 0 <= nr < 16 and 0 <= nc < 16 and not visited[nr][nc]:     # 범위를 벗어나지 않고 방문하지 않았을 때
                if arr[nr][nc] == 0:
                    queue.append((nr, nc))        # queue에 추가하고
                    visited[nr][nc] = 1   # 시작점까지의 칸수에 +1
                if arr[nr][nc] == 3:
                    visited[nr][nc] = 1
                    return 1
    # 반복문 종료되면 출발점 - 도착점 길 없다는것
    return 0



for _ in range(10):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]
    # 출발점, 도착점 먼저 찾기
    for i in range(1, 15):
        for j in range(1, 15):
            if maze[i][j] == 2:
                start = (i, j)
    result = bfs(maze, start)
    print(f'#{tc} {result}')
