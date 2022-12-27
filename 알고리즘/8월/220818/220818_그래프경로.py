def dfs(s, g):
    stack = []
    stack.append(s)
    visited[s] = 1
    while len(stack) != 0:          # 스택이 빌때까지 반복
        start = stack.pop()
        for w in arr[start]:        # 시작점과 연결된 노드 w를 탐색할건데
            if visited[w] == 0:     # 방문되어 있지 않은 노드가 있다면
                if w == g:
                    return True
                stack.append(w)
                visited[w] = 1
    return False

# 재귀로도 구현해보면
def dfs_2(s, g):
    global temp
    visited[s] = 1
    for w in arr[s]:
        if visited[w] == 0:     # 연결된 노드 중 방문되어 있지 않은 노드가 있다면
            if w == g:          # g에 방문하게 되면
                temp = True     # temp(그냥 임의의 변수)를 True로 바꿔줌
            dfs_2(w, g)         # 위 if문에 안걸리면 다시 재귀 실행


T = int(input())
for tc in range(1, T + 1):
    # V : 노드 개수 / E : 간선 개수 / arr : 노드간 연결 표시하는 2차원 그래프
    V, E = map(int, input().split())
    arr = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)
    for _ in range(E):
        # a, b 두 노드 사이의 간선 표시
        a, b = map(int, input().split())
        # arr 에 연결 표시하기
        arr[a].append(b)
    S, G = map(int, input().split())
    temp = False
    dfs_2(S, G)
    print(f'#{tc} {int(temp)}')
    # S부터 G까지 연결되어 있는지 확인!

