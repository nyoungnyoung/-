from collections import deque
def bfs(i, j):             # (i, j) : 시작지점
    # 상 / 하 / 좌 / 우 델타
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque([(i, j)])     # 시작지점 큐에 넣고 bfs 출발
    while queue:                # 큐가 빌때까지 반복해서
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N:
                # 기본 연료 1
                tmp = 1
                # 이동 전 높이와 이동 후 높이 비교해서 추가로 드는 연료 구하기
                if arr[x][y] < arr[nx][ny]:
                    tmp += arr[nx][ny] - arr[x][y]
                if cost[nx][ny] > cost[x][y] + tmp:
                    cost[nx][ny] = cost[x][y] + tmp
                    queue.append((nx, ny))
        return cost[-1][-1]



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cost = [[0xffffffff] * N for _ in range(N)]
    cost[0][0] = 0
    bfs(0, 0)
    print(cost)
    # print(f'#{tc} {result}')
