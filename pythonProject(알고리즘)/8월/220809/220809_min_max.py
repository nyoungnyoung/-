T = int(input())


for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    # 버블소트 진행
    for i in range(N-1, 0, -1):  # 구간 끝 정해주기
        for j in range(0, i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    result = lst[-1] - lst[0]
    print(f'#{tc} {result}')
