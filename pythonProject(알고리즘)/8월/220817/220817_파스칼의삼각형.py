# 크기가 N인 파스칼의 삼각형 (1 <= N <= 10)
# N = 4
# 0 [1, 0, 0, 0]    0열까지
# 1 [1, 1, 0, 0]    1열까지
# 2 [1, 2, 1, 0]    2열까지
# 3 [1, 3, 3, 1]    3열까지

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    for i in range(N):          # 모든 행에 대해
        for j in range(i+1):    # i열까지
            if j == 0:          # j가 0이면 arr[i][j]에 1 넣어주기
                arr[i][j] = 1
            else:               # 아니면 내 위쪽 행의 j-1열, j열 숫자 더해서 내 자리에 넣기
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
    print(f'#{tc}')
    for i in range(N):
        for j in range(i+1):
            print(arr[i][j], end = ' ')
        print()
