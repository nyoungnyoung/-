# T : 테스트케이스 수 / N : 보드의 한 변의 길이 / M : 돌을 놓는 횟수
# M 줄 : 돌을 놓을위치 / 돌의 색 (1 : 흑돌 / 2 : 백돌)
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [[0] * N for _ in range(N)]
    P = N // 2
    board[P-1][P-1], board[P][P] = 2, 2
    board[P-1][P], board[P][P] = 1, 1
    for m in range(M):
        *position, color = map(int, input().split())

