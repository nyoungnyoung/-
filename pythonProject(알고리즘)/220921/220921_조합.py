# 교재 p.46 10개의 원소 중에서 3개를 고르는 조합 생성
N = 10
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            print(i, j, k)