# 모든부분집합(powerset) / 부분집합(subset)
# 집합 A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# A의 부분집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수를 출력
# 해당하는 부분집합이 없는 경우 0 출력

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    cnt = 0

    # 부분집합 만들기
    n = len(A)
    for i in range(1<<n):        # 2^n-1만큼 반복해서
        sum_sub = 0
        sub_num = 0
        for j in range(n):       # 집합의 원소 수만큼 비트 생성, 비트 자리별로 1인지 비교
            if i & (1<<j):       # i의 j번 비트가 1인경우
                sum_sub += A[j]  # sum_sub에 j번원소를 더해준다
                sub_num += 1     # sub_num에 1을 더해준다
        if sum_sub == K and sub_num == N:
            cnt += 1
    print(f'#{tc} {cnt}')    
