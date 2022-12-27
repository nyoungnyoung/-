# 나보다 오른쪽에 있는 애들 중에 나보다 높이가 낮은 애가 몇개 있는지!

T = int(input())
for tc in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    result = 0                          # 낙차가 제일 큰 결과물 찾아야 하니까 변수 하나 선언
    for i in range(N - 1):
        cnt = 0                         # i번째 상자의 낙차 저장할 변수 선언
        for j in range(i + 1, N):
            if lst[i] > lst[j]:         # i번째 상자가 j번째 상자보다 높으면
                cnt += 1                # 낙차에 +1
            if result < cnt:            # max cnt를 구하고 싶은거니까
                result = cnt            # 반복문 종료될때마다 cnt와 result 값 비교해서 더 큰 값을 result에 저장
    print(f'#{tc} {result}')
