def bfs(s, g):
    queue = [s]                     # 큐 생성, 시작점 큐에 넣어주기
    while queue:                    # queue가 빌때까지 반복
        start = queue.pop(0)        # 큐의 첫번째 요소 pop해서 start로 설정
        # arr에서 start와 연결된 노드 중 방문하지 않은 노드 있는지 확인
        for w in arr[start]:        # start와 연결된 노드 w를 돌아보는데
            if not visited[w]:      # w를 방문하지 않았었다면
                queue.append(w)     # 큐에 넣고
                visited[w] = visited[start] + 1     # start의 visit 값에 +1
            if w == g:              # w가 목적지와 같으면
                return visited[w]   # w의 visited 값 반환
    return 0


T = int(input())
# 일단 노드 연결부터 표시해보자!
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    arr = [[] for _ in range(V + 1)]    # 인덱스 그대로 쓰기 위해서 V + 1개의 노드 만들기(0번은 비워둠)
    for _ in range(E):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)
    S, G = map(int, input().split())
    visited = [0] * (V + 1)             # 방문 처리해줄 리스트 생성
    result = bfs(S, G)
    print(f'#{tc} {result}')
