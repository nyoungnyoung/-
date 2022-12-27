# 인자로 받은 노드의 대표자 반환
def find_set(x):
    while x != parent[x]:
        x = parent[x]
    return x

# 인자로 받은 두 노드의 집합을 합치기(대표자의 번호를 똑같이 만들어주기)
def union(x, y):
    parent[find_set(y)] = find_set(x)


# 간선의 가중치를 기준으로 정렬
# 가중치가 작은 간선부터 선택
# 만약 사이클이 생긴다면(연결하려는 두 노드가 이미 같은 집합에 있으면) 선택하지 않음!

# 하나의 리스트에 넣고 정렬하기
V, E = map(int, input().split())
graph = []
for i in range(E):
    s, e, weight = map(int, input().split())
    graph.append((s, e, weight))

# 1. 가중치를 기준으로 정렬하기
graph = sorted(graph, key=lambda x:x[2])

# 2. 가중치가 작은거부터 간선 하나하나 선택해보기
MST = set()
target = 0

# V번까지 스스로가 부모인 노드들을 만들어주기
parent = [x for x in range(0, V+1)]

# graph[target]를 선택할지말지 결정!
# 노드 두개가 하나의 집합에 포함되어 있으면, 선택시 사이클이 생겨버림
# 노드 두개가 하나의 집합에 포함되지 않을 때만 선택해야 함!
while len(MST) < V:
    if find_set(graph[target][0]) != find_set(graph[target][1]):
        union(graph[target][0], graph[target][1])
        MST.add(graph[target])
    target += 1

print(MST)

'''
6 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''