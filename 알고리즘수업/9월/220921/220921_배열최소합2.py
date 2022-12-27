# SWEA 배열최소합 문제 다시 복습겸 순열 이용
# 이렇게 하는 이유? 시간 줄이려고...
def f(i, k, s):
    global minV
    if i == k:          # 인덱스 i == 원소의 개수
        if minV > s:
            minV = s
    elif s >= minV:     # 얘가 시간 줄여주는 코드!
        return
    else:
        for j in range(i, k):
            p[i], p[j] = p[j], p[i]
            f(i+1, k, s + arr[i][p[i]])       # i+1 자리를 결정하러 가봐~!
            # 자리 바꿨던거 원상복구 한 다음에 다시 자리 바꿔줘야함
            p[i], p[j] = p[j], p[i]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    p = [i for i in range(N)]         # p[i] : i행에서 선택한 열 번호
    minV = N * 10
    f(0, N, 0)
    print(f'#{tc} {minV}')