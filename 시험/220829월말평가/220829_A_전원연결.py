import sys
sys.stdin = open('전원연결_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 오른쪽 / 아래 / 왼쪽 / 위 델타 선언
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    for i in range(N):
        for j in range(N):
            # 0번째 행 / 열이 아니고 해당 요소가 1일때
            if i != 0 and j != 0 and arr[i][j] == 1:
                ni, nj = i, j
                for d in range(4):



    print(f'#{tc}')
