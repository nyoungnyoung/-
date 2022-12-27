# SWEA 배열최소합 문제 다시 복습겸 순열 이용
def f(i, k):
    global minV
    if i == k:      # 인덱스 i == 원소의 개수
        s = 0       # 모든 l행에서 p[l]열을 골랐을 때의 합
        for l in range(k):
            s += arr[l][p[l]]
        if minV > s:
            minV = s
    else:
        for j in range(i, k):
            p[i], p[j] = p[j], p[i]
            f(i+1, k)       # i+1 자리를 결정하러 가봐~!
            # 자리 바꿨던거 원상복구 한 다음에 다시 자리 바꿔줘야함
            p[i], p[j] = p[j], p[i]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    p = [i for i in range(N)]         # p[i] : i행에서 선택한 열 번호
    minV = N * 10
    f(0, N)
    print(f'#{tc} {minV}')

'''
input
3
3
2 1 2
5 8 5
7 2 2
3
9 4 7
8 6 5
5 3 7
5
5 2 1 1 9
3 3 8 3 1
9 2 8 8 6
1 5 7 8 3
5 5 4 6 8
'''
