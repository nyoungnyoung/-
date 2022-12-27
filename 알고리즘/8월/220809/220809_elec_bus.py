T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    # 정류장 만들기
    bus = [0] * (N+1)
    # 충전횟수
    cnt = 0
    # 충전소 위치 표시
    for i in lst:
        bus[i] = 1

    start = 0
    while start < N-K:
        go = K
        for i in bus[start+K:start:-1]:
            if i == 1:
                cnt += 1
                start += go
                break
            else:
                go -= 1
        else:
            cnt = 0
            break

    print(f'#{tc} {cnt}')




    # for i in range(N+1):
    #     start = 0
    #     for j in range(start, start+K+1):       # start부터 start+K까지의 구간 중에서 가장 멀리있는 i부터 다시 시작
    #         if bus[j] == 1:
    #             start = j
    #     print(start)









    # for i in range(1, len(lst)):
    #     if lst[i] - lst[i-1] > K:
    #         cnt = 0
    #         break
    #     else:
    #         for j in range(K, N-K+1):
    #             if bus[j] == 1:
    #                 cnt += 1
    # print(f'#{tc} {cnt}')

