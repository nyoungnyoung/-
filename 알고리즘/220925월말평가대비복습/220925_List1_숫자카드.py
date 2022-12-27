T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    card = list(map(int, input()))
    info = {}
    for i in card:
        if i not in info:
            info[i] = 1
        else:
            info[i] += 1
    print(info)
    print(max(info), info[max(info)])
    print(f'#{tc} ')
