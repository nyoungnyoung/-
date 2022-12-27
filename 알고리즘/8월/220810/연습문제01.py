T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

    # 사방 탐색을 위한 델타 준비
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    # 일단 반복문
    for i in range(N):
        for j in range(N):
            # mat[i][j] (i, j)를 중심으로 인접한 네 칸 조회
            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]
                if 0 <= ni < N and 0 <= nj < N:
                    print(mat[ni][nj])
