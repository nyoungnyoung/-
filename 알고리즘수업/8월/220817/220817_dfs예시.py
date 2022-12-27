adjList = [[1, 2],          # 0
           [0, 3, 4],       # 1
           [0, 4],          # 2
           [1, 5],          # 3
           [1, 2, 5],       # 4
           [3, 4, 6],       # 5
           [5]]             # 6

def dfs(v, N):
    visited = [0] * N       # visited 생성
    stack = [0] * N         # stack 생성
    top = -1
    print(v)                # 방문
    visited[v] = 1          # 시작점 방문 표시
    while True:
        for w in adjList[v]:
            if visited[v] == 0:     # if (v의 인접 정점 중 방문 안한 정점 w가 있으면)
                top += 1            # push(v)
                stack[top] = v
                v = w               # v <- w (w에 방문)
                print(v)            # 방문
                visited[w] = 1      # visited[w] <- True
                break
        else:                       # for문에서 break가 걸리지 않는다면(인접한 w가 없으면)
            if top != -1:           # 스택이 비어있지 않은 경우
                v = stack[top]      # pop
                top -= 1
            else:                   # 스택이 비어있으면
                break               # while문 중단!


dfs(0, 7)                    # 뭐지 왜 안돌아가지...?ㅠㅠ 교수님 코드 받아가지고 다시 시도해보자...
dfs(1, 7)