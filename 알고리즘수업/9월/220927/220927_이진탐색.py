T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    cnt = 0                 # 정수 개수 세주는 변수
    for i in B:
        l, r = 0, N - 1
        tmp = 0             # 어떤 구간 선택했지?(-1 : 왼쪽 / 1 : 오른쪽)
        # l이 r보다 작거나 같은동안 반복
        while l <= r:
            m = (l + r) // 2
            if A[m] == i:
                cnt += 1
                break
            # A[m]이 목표숫자보다 크면 왼쪽 구간 선택(tmp가 왼쪽이었을때는 break!)
            elif A[m] > i:
                r = m - 1
                if tmp == -1:
                    break
                else:
                    tmp = -1
            # A[m]이 목표숫자보다 작으면 오른쪽 구간 선택(tmp가 오른쪽이었을때는 break!)
            else:
                l = m + 1
                if tmp == 1:
                    break
                else:
                    tmp = 1

    print(f'#{tc} {cnt}')
