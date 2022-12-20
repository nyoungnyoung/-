# 교재 p.31 - 32 재귀호출을 통한 순열 생성 방법
def f(i, k):
    if i == k:      # 인덱스 i == 원소의 개수
        print(p)
    else:
        for j in range(i, k):
            p[i], p[j] = p[j], p[i]
            f(i+1, k)       # i+1 자리를 결정하러 가봐~!
            # 자리 바꿨던거 원상복구 한 다음에 다시 자리 바꿔줘야함
            p[i], p[j] = p[j], p[i]


N = 3
p = [i for i in range(1, N+1)]     # p = [i for i in range(1, 6)] 요렇게도 됨!
f(0, N)