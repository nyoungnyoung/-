def backtracking(i, s):           # i : 제품 개수 / s : 비용 합
    global minV
    if i == N:
        if minV > s:
            minV = s
    elif minV <= s:               # i가 N이 아닌데 minV보다 s가 크거나 같아지면 더이상 안해봐도 됨
        return
    else:
        for j in range(N):
            if not visited[j]:    # j에 방문한적 없으면
                visited[j] = 1    # 방문처리 하고 재귀 돌기!
                backtracking(i+1, s+cost[i][j])
                visited[j] = 0    # 재귀 끝나고 방문처리 해제



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    minV = 5000
    backtracking(0, 0)
    print(f'#{tc} {minV}')
