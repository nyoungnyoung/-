# r, c : 현재 위치
# dir : 움직이는 방향
# visited : 방문했던 카페에서 파는 디저트 set
def dfs(r, c, dir, visited):
    global max_val
    if visited and (r, c) == (i, j):        # 다른곳에도 방문한 적이 있고, (r, c)가 시작지점이면 멈춰라! 와 이렇게 하면 되는구나ㅜ
        # 한바퀴 돌아서 다시 도착한 경우를 검사하기 위해 visited 검사하는거!1
        # 제일 처음에는 visited가 비어 있을 것이기 때문...
        # 투어가 완료된 상황일 때 먹은 디저트의 길이 검사, max_val이랑 비교해서 더 큰 값 저장해주기!
        if max_val < len(visited):
            max_val = len(visited)
        return
    # 도착한 곳에서 파는 디저트가 이미 먹었던것이거나
    # 도착한 곳이 정상범위가 아닐경우 방향전환!(끝)
    if r < 0 or r >= N or c < 0 or c >= N or data[r][c] in visited:
        return
    # if문에 안걸렸으니까 일단 도착지점을 visited에 넣어줌!
    visited.add(data[r][c])

    # 직진 또는 다음 방향 이동
    # 직진 이동!
    dfs(r + dr[dir], c + dc[dir], dir, visited)
    # 방향 전환
    if dir < 3:     # 3인경우에는 방향전환하면 안됨
        dfs(r + dr[dir+1], c + dc[dir+1], dir+1, visited)

    # 도착한 곳에서 할 수 있는 건 다 해봤으니까 이제 visited에서 삭제해줘야 다른 경우 탐색 가능!
    visited.remove(data[r][c])


# 시계방향
dr = [1, 1, -1, -1]
dc = [1, -1, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    max_val = 0
    # 현재 내가 할 수 있는 건 다 해보자!!
    for i in range(N):
        for j in range(N):
            dfs(i, j, 0, set())
    print(f'#{tc} {max_val if max_val > 0 else -1}')
