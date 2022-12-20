from collections import deque
import sys

def dfs(v):
    visited[v] = 1          # 방문처리
    stack = deque([v])      # 첫번째 방문 노드 넣은채로 stack 만들기
    while stack:            # 스택이 빌때까지 반복해서
        n = stack.pop()         # 스택에서 노드를 하나 갖구와
        for i in tree[n]:       # n번 노드랑 연결되어있는 애들 중에
            if not visited[i]:  # 방문하지 않은 애가 있다면
                stack.append(i) # 얘를 스택에다가 넣고
                visited[i] = 1  # 방문처리해주자!
                parent[i] = n   # i번 노드보다 n번 노드를 먼저 방문했으니까, i의 부모노드는 n!

N = int(sys.stdin.readline())
# 0번 노드 x -> 첫번째 인덱스는 버리기 위해 N+1개 노드가 있는 트리 만들기
tree = [[] for _ in range(N+1)]
visited = [0] * (N+1)
parent = [0] * (N+1)    # 부모노드 저장해줄 리스트! parent[i] : i번 노드의 부모노드
# 트리의 연결 상태 표현해주기! tree[i] : i번 노드에 연결된 노드들
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

print(tree)

dfs(1)  # 1번 노드부터 방문시작! -> parent에 부모노드 정보 저장됨!
print(parent)
for i in range(2, N+1):
    print(parent[i])