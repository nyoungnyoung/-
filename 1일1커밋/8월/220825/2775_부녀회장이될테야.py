# a층 b호에 살려면 (a-1)층 1~b호 사람 수의 합만큼 사람들을 데려와 살아야함
# 비어있는 집 없을 대 k층 n호에 몇명이 살고있는지 출력
# 0층부터 있고, 각 층에는 1호부터 있음
# 0층의 i호에는 i명이 산다.

T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    people = [_ for _ in range(1, n + 1)]    # 0층 : 1호~n호 까지의 사람 수
    for i in range(k):
        for j in range(1, n):
            people[j] += people[j-1]
    print(people[-1])
