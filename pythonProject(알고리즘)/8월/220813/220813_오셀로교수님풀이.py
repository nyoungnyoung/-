T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 돌을 놓을 수 있는 배열 준비
    # 흑돌 1, 백돌 2
    # 0행과 0열은 사용하지 않고, 문제에서 주어지는 좌표와 실제 위치를 맞추기 위해
    # (N+1) * (N+1) 크기의 배열 준비
    board = [[0] * (N+1) for _ in range(N+1)]
    center = N // 2
    board[center][center] = 2
    board[center+1][center+1] = 2
    board[center+1][center] = 1
    board[center][center+1] = 1

    # 8방 탐색을 위해 델타배열 준비
    dr = [-1, -1, 0, 1, 1, 1, 0, -1]
    dc = [0, 1, 1, 1, 0, -1, -1, -1]


    # M개의 돌의 위치가 주어짐
    for i in range(M):
        c, r, color = map(int, input().split())
        # (r,c)에 돌을 놓을건데
        board[r][c] = color
        # 8방을 탐색하면서, 색깔을 바꿀 수 있는 돌이 있는지 탐색
        for d in range(8):
            # 각 방향으로 진행하면서, 같은 색깔 돌 찾기
            # 같은 색 돌을 찾으면 원래 자리로 돌아오면서 색 바꾸기
            # 만약 같은색 돌 찾기 전에 빈칸을 만나거나,
            # 범위를 벗어나면 아무작업도 하지 않음
            nr = r + dr[d]
            nc = c + dc[d]
            while True:
                if nr < 1 or nr > N or nc < 1 or nc > N or board[nr][nc] == 0:
                    # 아무 작업도 안함
                    break
                if board[nr][nc] == color:
                    # 원래 자리로 돌아오면서 색 바꾸기
                    while (nr, nc) != (r, c):
                        nr -= dr[d]
                        nc -= dc[d]
                        board[nr][nc] = color
                    break
                nr += dr[d]
                nc += dc[d]

    # 흰돌, 까만돌 개수세기
    w_cnt = 0
    b_cnt = 0
    for i in range(N+1):
        for j in range(N+1):
            if board[i][j] == 2:
                w_cnt += 1
            elif board[i][j] == 1:
                b_cnt += 1
    print(f'#{tc} {b_cnt} {w_cnt}')
