# 1 : 흑돌 / 2 : 백돌

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [[0] * (N + 1) for _ in range(N + 1)]
    # 처음 돌 4개 세팅
    board[N // 2][N // 2], board[N // 2 + 1][N // 2 + 1] = 2, 2
    board[N // 2][N // 2 + 1], board[N // 2 + 1][N // 2] = 1, 1
    for _ in range(M):
        x, y, color = map(int, input().split())
        board[x][y] = color

        # 8방향 델타 선언(위쪽부터 시계방향)
        dx = [-1, -1, 0, 1, 1, 1, 0, -1]
        dy = [0, 1, 1, 1, 0, -1, -1, -1]

        # 주어진 (x,y)좌표부터 델타탐색 시작!
        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]
            reverse = []  # 뒤집을 돌 위치 저장해 줄 리스트
            while True:
                # (nx, ny)가 범위 벗어나지 않고, board[nx][ny]가 0이 아니면
                if 0 < nx < N + 1 and 0 < ny < N + 1 and board[nx][ny]:
                    # (x, y)좌표의 돌 색이랑 비교해서 색이 다르면 그 방향으로 계속 탐색ㄱㄱ
                    if board[nx][ny] != board[x][y]:
                        reverse.append((nx, ny))
                        nx += dx[d]
                        ny += dy[d]
                    # (x, y)좌표의 돌 색이랑 같아지면 break, while문 밖에서 reverse에 들어있는 돌들 다 바꿔주기
                    else:
                        break
                # 범위 벗어나거나, 돌이 없으면 reverse 초기화, while문 종료
                else:
                    reverse = []
                    break
            for i, j in reverse:
                board[i][j] = board[x][y]

    cnt_1, cnt_2 = 0, 0
    for i in range(N + 1):
        for j in range(N + 1):
            # 흑돌이면
            if board[i][j] == 1:
                cnt_1 += 1
            # 백돌이면
            if board[i][j] == 2:
                cnt_2 += 1
    print(f'#{tc} {cnt_1} {cnt_2}')