# 1번째큰수, 1번째작은수, 2번째큰수, 2번째작은수 ....
# 이렇게 정렬한 결과를 10개까지만 출력하기
# 이거는 선택정렬 응용하면 될듯? 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    for i in range(10):         # 서치 구간의 시작점 i정하기 (10번째까지만 출력하니까 range10)
        min_idx, max_idx = i, i
        for j in range(i, N):    # 시작점 i부터 list 끝까지 min / max 서치
            if arr[max_idx] < arr[j]:
                max_idx = j              
            if arr[min_idx] > arr[j]:
                min_idx = j
        if i % 2 == 0:      # i가 짝수면 max랑 자리바꾸기
            arr[i], arr[max_idx] = arr[max_idx], arr[i]
        else:               # i가 홀수면 min이랑 자리바꾸기            
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    result = ' '.join(map(str, arr[:10])) 

    print(f'#{tc} {result}')