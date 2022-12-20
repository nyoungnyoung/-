T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    max_num, min_num = lst[0], lst[0]
    for i in lst:
        if max_num < i:
            max_num = i
        if min_num > i:
            min_num = i
    result = max_num - min_num
    print(f'#{tc} {result}')
