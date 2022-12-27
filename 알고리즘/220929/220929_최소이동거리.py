def dijkstra(v):         # 다익스트라 구현할때는 시작점이 중요함!!(v : 출발노드)
    # v에서 각 노드로 갈 수 있는 비용을 저장한 w를 준비
    w = adj[v][:]       # v와 인접한 행렬 정보를 가져오겠다
    # w에서 제일 작은 비용을 가지는 노드를 선택
    # 그 노드를 선택해서 만들어지는 경로 비용 재계산하기

    pass

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    # 0~N번까지
    adj = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(E):
        s, e, d = map(int, input().split())
        adj[s][e] = d
    # 0번노드에서 N번 노드로 가는 최소 비용 구하기
    dijkstra(0)