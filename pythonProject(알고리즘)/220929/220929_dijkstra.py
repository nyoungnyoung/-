'''
5 11
0 1 3
0 2 5
1 2 2
1 3 6
2 1 1
2 3 4
2 4 6
3 4 2
3 5 3
4 0 3
4 5 6
'''
# 각 노드로 가기 위한 최단경로(최소비용) 구하기
V, E = map(int, input().split())
adj = [[0xffffffff] * (V+1) for _ in range(V+1)]
for i in range(E):
    s, e, weight = map(int, input().split())
    adj[s][e] = weight

def dijkstra(start):
    # 각 노드로 가는 비용이 싼 노드들을 하나씩 선택하면서,
    # 갈 수 있는 경로가 있고, 비용이 기존 경로보다 더 싸면 업데이트 해 주기

    # distance : start에서 각 노드로 가는 비용(인접행렬의 start를 복사해서 가져옴)
    distance = adj[start][:]
    # # selected : 이미 선택한 정점을 표시하기 위한 집합
    # selected = set([start])
    # selected대신 visited로 이미 선택한 정점 표시
    visited = [0] * (V+1)
    visited[start] = 1
    distance[start] = 0
    while sum(visited) <= V:            # selected 유니온으로 하면 이렇게 안해도 될듯?
        min_idx = 0
        min_val = 0xffffff
        for i in range(V+1):
            if not visited[i] and distance[i] < min_val:
                min_idx = i
                min_val = distance[i]
        # 최소 비용을 가지는 노드를 안다!
        visited[min_idx] = 1
        # 방금 선택된 노드를 거쳐서 갈 수 있는 노드들의 방문비용 확인
        # 직통으로 가는것보다 내가 선택한 노드 지나쳐서 가는게 더 이득이다? 업뎃
        for i in range(V+1):
            if not visited[i] and distance[i] > min_idx + adj[min_idx][i]:
                distance[i] = min_val + adj[min_idx][i]
    return distance

result = dijkstra(0)
print(result)