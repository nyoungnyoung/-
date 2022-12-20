T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    attack = [[0] * N for _ in range(N)]        # 공격 당하거나 방어탑이 있는 위치 기록해줄 2차원 배열
    top = []

    # 상 / 하 / 좌 / 우 델타 선언
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # graph 돌면서 2(방어탑)가 있는 곳 / 1(장애물) 먼저 찾아보기
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 2:
                top.append((i, j))
                attack[i][j] = 1
            if graph[i][j] == 1:
                attack[i][j] = 1

    # top의 위치부터 델타 탐색하기(공격할 수 있는 곳이면 attack 1표시)
    for idx in top:
        x, y = idx
        # graph에서 1이나 2, 벽을 만날때까지 계속 그 방향으로 탐색해야함
        for d in range(4):
            j = 1
            while True:
                nx = x + dx[d] * j
                ny = y + dy[d] * j
                # 1, 2, 벽(범위 밖) 만나면 이 방향 델타탐색 종료
                if nx < 0 or nx >= N or ny < 0 or ny >= N or graph[nx][ny]:
                    break
                # 위 if문에 안걸렸고, attack이 0이고, graph[nx][ny]가 0이면 공격가능
                if not attack[nx][ny] and not graph[nx][ny]:
                    attack[nx][ny] = 1
                j += 1

    # 다 돌고나면 attack에서 공격당하지 않은 곳 갯수 세주기
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not attack[i][j]:
                cnt += 1

    print(f'#{tc} {cnt}')

