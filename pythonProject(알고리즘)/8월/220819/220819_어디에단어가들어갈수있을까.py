import sys
sys.stdin = open('어디에단어_input.txt', 'r')
T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    # 가로
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
            if arr[i][j] == 0 or j == N - 1:    # 해당 칸이 0이거나 마지막 열일경우
                if cnt == K:                    # cnt가 단어 길이와 같다면
                    result += 1
                cnt = 0
    # 세로
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[j][i] == 1:
                cnt += 1
            if arr[j][i] == 0 or j == N - 1:
                if cnt == K:
                    result += 1
                cnt = 0
    print(f'#{tc} {result}')
