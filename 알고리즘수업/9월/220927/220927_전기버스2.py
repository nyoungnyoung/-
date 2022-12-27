def backtracking(i, cnt):     # i : 정류장 / cnt : 교환횟수
    global min_change
    if i >= N - 1:                # 정류장 번호 넘어가면 min값이랑 cnt 비교해서 더 작은값 저장
        if min_change > cnt:
            min_change = cnt
        return
    elif min_change <= cnt:   # 그 경우가 아닌데 min값보다 cnt가 더 클때는 더이상 진행x
        return
    else:
        for j in range(lst[i]):
            backtracking(i+j+1, cnt+1)      # i+j만큼 이동한 정류장에서 다시 살펴보자! 근데 리스트의 첫번째 인덱스는 N이니까 +1


T = int(input())
for tc in range(1, T + 1):
    lst = list(map(int, input().split()))
    N = lst.pop(0)
    min_change = 100        # 최소 교환 횟수
    backtracking(0, -1)
    print(f'#{tc} {min_change}')