T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    # 봉우리 개수 세 줄 변수 선언
    cnt = 0
    # lst의 원소를 돌아볼건데,
    for i in range(len(lst)):
        # N == 1일때는 무조건 봉우리 1개
        if N == 1:
            cnt = 1
            break
        # N != 1일때 (lst 길이가 1보다 클때)
        else:
            # 제일 첫번째 원소(i == 0)라면, 다음 원소(i + 1)보다 크면 cnt + 1
            if i == 0 and lst[i] > lst[i+1]:
                cnt += 1
            # 제일 마지막 원소(i == N - 1)라면, 이전 원소(i - 1)보다 높으면 cnt + 1
            elif i == N - 1 and lst[i] > lst[i-1]:
                cnt += 1
            # 둘다 아니면
            else:
                # 이전 원소(i - 1)보다 크거나 같고, 다음 원소(i + 1)보다 크거나 같을때 cnt + 1
                if lst[i] >= lst[i-1] and lst[i] >= lst[i+1]:
                    cnt += 1
                    # 연속된 봉우리 빼주기 위해 이전 원소와 같을 경우 cnt - 1
                    if lst[i] == lst[i-1]:
                        cnt -= 1
    print(f'#{tc} {cnt}')

