T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    container.sort(reverse=True)
    truck.sort(reverse=True)
    result = 0
    for i in truck:
        for j in container:
            if i >= j:
                result += j
                container.remove(j)
                break
    print(f'#{tc} {result}')