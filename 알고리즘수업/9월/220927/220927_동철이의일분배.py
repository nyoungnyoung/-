def backtracking(i, p):
    global max_p
    if i == N:
        if max_p < p:
            max_p = p
    elif max_p >= p:
        return
    else:
        for j in range(N):
            if not visited[j]:  # j에 방문한 적 없으면
                visited[j] = 1
                backtracking(i+1, p*arr[i][j]*0.01)
                visited[j] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    max_p = 0
    backtracking(0, 1)
    print(f'#{tc} {max_p*100:.6f}')
