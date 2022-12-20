T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    room = []
    for _ in range(N):
        room.append(list(map(int, input().split())))

    # 최대 방문할 수 있는 방 개수 max_cnt / 처음 출발하는 방 번호 result 초기화해주기
    max_cnt = 0
    result = room[0][0]

    # 상/하/좌/우 델타 선언
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # (0, 0)부터 (x, y) 좌표 정해준 후에 해당 지점부터 상하좌우 델타 탐색하기!
    for i in range(N):
        for j in range(N):
            x, y = i, j
            # start = room[x][y]
            cnt = 1             # 방문한 방 수 세어줄 변수 cnt에 처음 방 개수 넣어주기
            while True:
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    # nx, ny가 범위를 넘어가지 않고, room[nx][ny]가 room[x][y]보다 정확히 1 클때 cnt + 1
                    if 0 <= nx < N and 0 <= ny < N and room[nx][ny] == room[x][y] + 1:
                        cnt += 1
                        x, y = nx, ny
                        break
                else:
                    break
            # cnt랑 max_cnt 비교해서 더 크면 max_cnt에 저장, result랑 처음 방 번호 비교해서 더 작은 값 저장
            if max_cnt < cnt:
                max_cnt = cnt
                result = room[i][j]
            if max_cnt == cnt:
                if result > room[i][j]:
                    result = room[i][j]
    print(f'#{tc} {result} {max_cnt}')
