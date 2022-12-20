# 교재 p.33 - 34 재귀호출&used배열 활용 순열 생성 방법
# nPr을 만들건데, 제일 앞자리 1개는 고정시키고 싶어!
def f(i, k, r):        # i : 시작하는 인덱스 / k : 총 원소개수 / r : 내가 고르고 싶은 원소 개수
    if i == r:
        print(p)
    else:
        for j in range(k):
            if used[j] == 0:    # a[j]가 아직 사용되지 않았으면
                used[j] = 1     # a[j]가 사용됨으로 표시
                p[i] = a[j]     # p[i]는 a[j]로 결정
                f(i+1, k, r)    # p[i+1] 값을 결정하러 이동
                used[j] = 0     # a[j]를 다른 자리에서 쓸 수 있도록 해제하기


N = 5
R = 3
a = [i for i in range(1, N+1)]
used = [0] * N
p = [0] * R
# 요부분!! 중간 고정도 얘랑 비슷하겠지ㅎㅎ
p[0] = 1
used[0] = 1
f(1, N, R)