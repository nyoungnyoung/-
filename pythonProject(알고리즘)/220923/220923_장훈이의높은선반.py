T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))
    h = len(height)
    sum_lst =[]
    for i in range(1, 1 << h):
        tmp = 0
        for j in range(h):
            if i & (1 << j):
                tmp += height[j]
        sum_lst.append(tmp)
    sum_lst = list(set(sum_lst))
    lst = []
    for i in sum_lst:
        if i >= B:
            lst.append(i)
    result = min(lst) - B
    print(f'#{tc} {result}')

