import sys
sys.setrecursionlimit(10000)                       # N 이 100000 만큼 있어서 limit 를 그만큼 늘려주셔야 할 것 같습니다. (dfs 라서 N 만큼 호출 할 가능성이 있습니다.)
N, M, R = map(int, sys.stdin.readline().split())
order = []  # 방문순서


# dfs 함수 만들기
def dfs(g, s, visited):
    # 시작노드 방문처리
    visited[s] = True
    order.append(s)
    for i in g[s]:  # 현재 노드와
        if not visited[i]:   # 연결된 노드가 방문되지 않았을 경우
            dfs(g, i, visited)


visited = [False] * (N+1)

graph = [[] for _ in range(N+1)]
# 그래프 만들기
for i in range(N):      # N줄 반복                  --> # 간선의 개수는 M 이므로 M 만큼 반복 하여야 할 것 같습니다.
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(len(graph)):
    graph[i].sort()

dfs(graph, 1, visited)               # 저도 했던 실수 인데, 시작 지점이 항상 1은 아닙니다. 시작 정점이 주어지니 그것을 활용하면 됩니다.
for i in range(N):
    if i == N-1:                    # 구현 하신 dfs 에서
        print(0)                    # order 은 다음과 같은 식으로 만들어지기 때문에 왼쪽 처럼 print 하시면 아마 답이 안나올 것 같습니다.
    else:                           # 정점이 1~9 까지 있고 3번부터 시작 3-5-7-9 순으로 탐색 끝
        print(order[i])             # order = [3,5,7,9]
                                    # print(3) -> print(5) -> print(7) -> print(9) ->  (아직 8번 반복 안했기 때문에) print(order[4]) : index_error
                                    # 출력을 바꾸시거나 order 에 담는 방식을 조금 바꾸시는게 좋을 것 같습니다. ex) order = [0]*10 -> dfs
                                    # -> order = [0,0,0,1,0,2,0,3,0,4]
