T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    time_table = []
    cnt = 1  # 화물차 개수 세는 변수
    for _ in range(N):
        time = tuple(map(int, input().split()))
        time_table.append(time)
    time_table.sort(key=lambda x: x[1])
    i = 0
    for j in range(1, N):
        if time_table[i][1] <= time_table[j][0]:    # 시작시간이 종료시간보다 늦거나 같을경우
            cnt += 1
            i = j
    print(f'#{tc} {cnt}')

