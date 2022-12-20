# 보너스 상금 획득할 수 있는 기회
# 주어진 숫자판 중 두개를 선택해 정해진 횟수만큼 서로의 자리를 교환할 수 있다.
# 정해진 횟수만큼 교환이 끝나면 숫자판만큼의 상금 획득
# 반드시 횟수만큼 교환이 이루어져야 함

# 이거 nPn 자리바꾸는 방법으로 구했던거 응용 하면 될거같음!
# 대신 자리바꾸는건 N번만큼만 반복

def change(i, c):                           # i : 시작인덱스 / c : 반복횟수
    global result
    if c == N:
        result = max(int(''.join(P)), result)
        return
    for j in range(i, len(P)):              # j : i ~ len(P) 시작인덱스부터 끝까지
        for k in range(j+1, len(P)):        # k : j+1 ~ len(P) j 오른쪽부터 끝까지
            if P[j] <= P[k]:                # 뒤쪽값이 더 크면 자리바꾸기!
                P[j], P[k] = P[k], P[j]
                change(j, c+1)              # 반복횟수 + 1하고 재귀호출
                P[j], P[k] = P[k], P[j]     # 다시 자리 바꿔주기
    if result == 0 and c < N:   # 정해진 교환횟수 못채웠을 경우(남은 교환횟수가 짝수면 그대로 두고, 홀수면 젤 끝자리 두개 변경)
        if (N - c) % 2:         # 홀수면 젤끝자리 두개 바꿔주기
            P[-1], P[-2] = P[-2], P[-1]
        change(i, N)            # 결과 내주기위해 change(i, N) 호출 -> 첫번째 if에 걸려서 return


T = int(input())
for tc in range(1, T + 1):
    P, N = input().split()    # 숫자판 정보(최대 6자리) / 교환 횟수(최대 10)
    P, N = list(P), int(N)
    result = 0
    change(0, 0)
    print(f'#{tc} {result}')
