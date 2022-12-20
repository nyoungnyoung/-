def dfs(v, s):              # v : 현재 노드 / s : 합
    global minV
    if visited == [1] * N:  # 전부다 방문했으면 멈추고 v -> 0 가는 거 s에 더해주기
        s += arr[v][0]
        if minV > s:
            minV = s
            s -= arr[v][0]
            visited[v] = 0
        return
    for node in graph[v]:           # 현재 노드와 인접한 노드 확인할건데
        if not visited[node[0]]:    # 방문하지 않았다면
            visited[node[0]] = 1    # 노드 방문처리
            dfs(node[0], s + node[1])
            visited[node[0]] = 0    # 방문처리 취소

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    graph = []      # 연결리스트
    minV = 2000
    for i in range(N):
        line = []
        for j in range(N):
            if arr[i][j] != 0:
                line.append((j, arr[i][j]))
        graph.append(line)
    visited = [0] * N
    visited[0] = 1
    dfs(0, 0)
    print(f'#{tc} {minV}')

