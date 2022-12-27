T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 파리 수 합 저장할 리스트 생성
    lst = []
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            sum_fly = 0                 # 파리 수의 합
            for di in range(M):         # M * M 구간 내 탐색하기 위한 di / dj
                for dj in range(M):
                    sum_fly += arr[i + di][j + dj]
            lst += [sum_fly]            # lst에 파리 수의 합 추가해주기
    result = max(lst)
    print(f'#{tc} {result}')
