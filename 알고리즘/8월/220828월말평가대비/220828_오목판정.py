import sys
sys.stdin = open('오목판정_input.txt', 'r')


def is_omok(arr):
    # 가로줄 / 세로줄 / 오른족 아래 대각선/ 왼쪽 아래 대각선 델타 선언
    di = [0, 1, 1, 1]
    dj = [1, 0, 1, -1]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                for d in range(4):
                    ni = i
                    nj = j
                    cnt = 0             # o 갯수 세어줄 변수
                    while 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'o':
                        cnt += 1
                        ni += di[d]
                        nj += dj[d]
                    if cnt >= 5:
                        return 'YES'
    return 'NO'


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input().strip()) for _ in range(N)]
    result = is_omok(arr)
    print(f'#{tc} {result}')
