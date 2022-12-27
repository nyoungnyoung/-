def find_maze(arr, s, g):
    # 상/ 하 / 좌 / 우 델타 선언
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    # 큐 만들어주고 시작점 넣어줌
    queue = [s]
    while queue:                # 큐가 빌때까지 반복
        sr, sc = queue.pop(0)   # 방문하자마자 바로 pop해서 시작지점의 r, c값 튜플에서 받아오기
        visited[sr][sc] = 1     # 시작점 방문처리
        for d in range(4):
            # 시작점의 상하좌우 돌면서 0이 있고 방문하지 않은곳이면 갈 수 있음
            nr, nc = sr + dr[d], sc + dc[d]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:     # 범위를 벗어나지 않고 방문하지 않았을 때
                if arr[nr][nc] == 0:
                    queue.append((nr, nc))        # queue에 추가하고
                    distance[nr][nc] = distance[sr][sc] + 1   # 시작점까지의 칸수에 +1
                if arr[nr][nc] == 3:
                    distance[nr][nc] = distance[sr][sc]
                    return distance[nr][nc]
    # 반복문 종료 후 도착지점의 distance 값
    return 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input().strip())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    distance = [[0] * N for _ in range(N)]
    # 0 : 통로 / 1 : 벽 / 2 : 출발 / 3 : 도착
    # 출발지점이랑 도착지점부터 찾아보자
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = (i, j)
            if maze[i][j] == 3:
                goal = (i, j)
    result = find_maze(maze, start, goal)
    print(f'#{tc} {result}')
