# 교재 p.47 n개의 원소 중에서 r개를 고르는 조합
# 재귀적으로 구현!
def nCr(n, r, s):   # s: 선택할 수 있는 구간의 시작
    if r == 0:
        print(*comb)
    else:
        for i in range(s, n-r+1):
            comb[r-1] = A[i]
            nCr(n, r-1, i+1)

A = [1, 2, 3, 4, 5]
n = len(A)
r = 3
comb = [0] * r
nCr(n, r, 0)