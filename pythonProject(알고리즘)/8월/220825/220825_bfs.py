def bfs():
    # bfs는 재귀가 안됨!!
    # dfs는 스택 구조를 이용하는 것이였기 때문에, 스택과 비슷한 작동을 하는 재귀로 구현할 수 있었던 것임
    queue = [0]
    visited[0] = 1      # 방문표시
    # 노드에 방문해서(방문하면 즉시 pop - 다시 되돌아올 필요가 없기 때문)
    # 해당 노드에서 방문할 수 있는 노드가 있으면 queue에 다 넣어주기
    # 큐가 비어있지 않으면 계속 위 작업 반복(큐가 비어있으면 종료)
    while queue:
        front = queue.pop(0)
        print(front, end=' ')       # 방문하는 순서 보고 싶다면 요 부분 확인
        # if front == 목적지? 요런 작업도 여기서 할 수 있다!
        # 현재 노드에서 갈 수 있는 모든 경로 찾기
        for i in range(N):
            if adj[front][i] == 1 and not visited[i]:       # 이면 내가 방문할 수 있는 경로임!!
                queue.append(i)
                visited[i] = 1      # 방문처리


V, E = map(int, input().split())
N = V + 1
adj = [[0] * N for _ in range(N)]
for _ in range(E):
    a, b = map(int, input().split())
    adj[a][b] = 1
    adj[b][a] = 1
visited = [0] * N
bfs()


# dfs참고
# arr = [
# [2,1,0,0,1],
# [0,1,0,0,1],
# [2,1,1,1,1],
# [0,1,0,0,1],
# [0,2,0,0,2]
# ]
#
# N = len(arr)
# min_distance = 0xfffffff
# #반복+stack을 이용한 dfs
# def dfs(sr, sc):
#     global min_distance
#     stack = [(sr, sc, 0)]
#     visited = [[0]*N for _ in range(N)]
#     visited[sr][sc] = 1
#     while stack:
#         #현재 위치: stack의 top
#         # 에서 갈 수 있는 경로 모조리 찾아보기
#         # r, c, distance = stack[-1]    #dfs
#         r, c, distance = stack.pop(0)   #bfs
#         if arr[r][c] == 2:
#             print('찾았다!',(r,c,distance))
#             return distance
#             # return 1
#         for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
#             nr, nc = r + dr, c + dc
#             #정상범위안에 있으면서, 갈수 있는 길이고, 방문하지 않은경우
#             if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] and not visited[nr][nc]:
#                 stack.append((nr, nc,distance+1))
#                 visited[nr][nc] = 1
#                 # break #dfs
#         # else:     #dfs
#         #     stack.pop()
#     return 0
#
#
# visited = [[0]*N for _ in range(N)]
#
# def dfs2(r,c,distance):
#     visited[r][c] = 1
#     if arr[r][c] == 2:
#         return distance
#     min_distance = 0xffffff
#     for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#         nr, nc = r + dr, c + dc
#         # 정상범위안에 있으면서, 갈수 있는 길이고, 방문하지 않은경우
#         if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] and not visited[nr][nc]:
#             result = dfs2(nr,nc,distance+1)
#             if min_distance > result:
#                 min_distance = result
#     return min_distance
#
# # print(dfs(0,1))
# # print(min_distance)
#
# print(dfs2(0,1,0))