'''
1. 시작점을 stack에 넣어줌
2. stack의 top에 있는 정점에서 인접한 노드 중, 방문하지 않은 노드 찾기
3.
    3-1 : 2에 해당하는 노드를 찾았다면 방문(stack에 push) 처리 후, 2번을 중단
    3-2 : 2에 해당하는 노드를 못찾았다(경로를 못찾음)(stack pop)
4. 2번으로 돌아가서 반복(stack이 비어있지 않으면 계속 반복)

마지막 정점번호 6 V, 간선수 8 E
6 8
0 1
0 2
1 3
2 4
3 5
4 5
5 6
'''


def dfs(graph):
    start = 0
    stack = []
    stack.append(start)     # 시작점으로부터 dfs수행하기 위해 시작점을 stack에 넣어줌
    # 방문했던 노드는 다시 방문하지 않음
    # 노드를 방문했음을 표시하는 배열 - 0 : 미방문, 1 : 방문
    visited = [0] * (V + 1)
    visited[start] = 1      # 시작점 방문표시
    # 현재 노드에 인접하면서 방문하지 않은 노드 찾고, stack에 push
    # 경로 없으면 stack에서 pop
    # 위 과정을 stack이 비어있지 않으면 계속 반복
    # python에서 배열 >> 참거짓으로 바꾸면...비어있으면 False / 요소가 있으면 True
    while len(stack) > 0:           # while stack: 이렇게 쓰면 더 깔끔함(요소가 있으면 계속 반복해라)
        top = stack[-1]
        print(top)
        for i in range(N):
            # graph[top][i] == 1 and visited[i] == 0 이랑 같음
            if graph[top][i] and not visited[i]:  # top이랑 i가 연결되어 있고 방문하지 않았다면
                stack.append(i)
                visited[i] = 1
                break       # 경로찾기 중단
        else:               # break가 한번도 안걸림 == 경로 찾지 못함
            stack.pop()




V, E = map(int, input().split())
N = V + 1
graph = [[0] * N for _ in range(N)]
for _ in range(E):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    # 왜 이렇게 하시지..? 이러면 더 어렵지 않나..?
for row in graph:
    print(row)
