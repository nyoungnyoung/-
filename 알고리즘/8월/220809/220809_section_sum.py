T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input(). split()))
    sum_list = []
    for i in range(N-M+1):
        sum_num = 0
        for j in range(i, i+M):
            sum_num += lst[j]
        sum_list.append(sum_num)
    # sum_list 버블소트 시작
    for i in range(len(sum_list)-1, 0, -1):
        for j in range(i):
            if sum_list[j] > sum_list[j+1]:
                sum_list[j], sum_list[j+1] = sum_list[j+1], sum_list[j]
    result = sum_list[-1] - sum_list[0]
    print(f'#{tc} {result}')



