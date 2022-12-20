# kruskal 알고리즘 이용!
# x의 parent 노드번호 반환
def find_set(x):
    while x != parent[x]:
        x = parent[x]
    return x                # 자기 자신이 대표번호면 x 그대로 반환


# x, y가 포함된 집합 합치기! 대표 번호 똑같게 만들어주면 됨
def union(x, y):
    parent[find_set(y)] = find_set(x)


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    graph = []
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        graph.append((n1, n2, w))
    # w 기준으로 오름차순 정렬!
    graph = sorted(graph, key=lambda x:x[2])
    # w가 제일 낮은거부터 하나씩 선택해보기
    parent = [x for x in range(V+1)]  # 0~V번까지 스스로가 대표자인 노드 만들기
    MST = set()
    idx = 0
    while len(MST) < V:     # V-1개의 간선 선택될때까지 반복
        # 주어진 노드 n1, n2가 같은 집합에 포함되어 있지 않을때만 선택!!
        # 선택하면 MST에 넣어주고 n1, n2 같은 집합으로 만들어줘야함!
        if find_set(graph[idx][0]) != find_set(graph[idx][1]):
            MST.add(graph[idx][2])
            union(graph[idx][0], graph[idx][1])
        idx += 1
    result = 0
    for i in MST:
        result += i[2]
    print(f'#{tc} {result}')
