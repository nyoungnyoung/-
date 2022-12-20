def dfs(x, y, s):           # dfs함수에 x, y좌표와 함께 지나온 길의 합 넘겨주기
    global minV
    s += arr[x][y]          # s에 arr[x][y]의 값 더해주기
    # 아래/오른쪽 델타
    dx = [1, 0]
    dy = [0, 1]
    if x == N - 1 and y == N - 1:   # 마지막 칸에 도착하면
        if s < minV:                # 합이랑 minV 비교해주고, s가 더 작으면 minV 교체
            minV = s
        return                      # 돌아가!
    for d in range(2):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < N and 0 <= ny < N:     # 범위 넘어가지 않으면
            dfs(nx, ny, s)                  # 다음 칸에서 dfs함수 재귀호출


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    minV = 1700     # 주어진 입력값의 범위에 의해 1690 이상의 값은 나오지 않음
    dfs(0, 0, 0)
    print(f'#{tc} {minV}')
