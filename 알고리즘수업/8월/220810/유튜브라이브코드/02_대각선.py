# 행, 열
# 0, 0
# 1, 1
# 2, 2
# 3, 3
# 의 합(왼쪽 아래로 향하는 대각선의 합)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]


s = 0
for i in range(N):
    for j in range(N):
        if i == j:
            s += arr[i][j]

s = 0
for i in range(N):
    s += arr[i][i]
# 두번째 방법이 조금 더 효율적


# 반대방향 대각선의 합
# 0, 3  = 3
# 1, 2  = 3
# 2, 1  = 3
# 3, 0  = 3

s = 0
for i in range(N):
    s += arr[i][N-1-i]


# 그러면 양 대각선의 합은?
# N이 홀수일때는 가운데에 위치한 애를 두번 더하게 되므로 한번은 빼줘야함
# N // 2
# 생각해보기
