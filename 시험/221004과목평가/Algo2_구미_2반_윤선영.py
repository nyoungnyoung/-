T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    jewel = list(map(int, input().split()))

    # 수집하는 보석 리스트(52개->이정도면 for문 다 돌아도 괜찮을듯?) 만들어볼까?
    wanted = [4, 6, 7, 9, 11]
    wanted_lst = set()
    for i in wanted:
        j = 1
        while i * j <= 100:
            wanted_lst.add(i*j)
            j += 1

    # jewel 내에서 수집 안하는 보석 뺀 리스트 새로 만들기
    lst = []
    for i in jewel:
        if i in wanted_lst:
            lst.append(i)

    # lst의 부분집합 구하고 걔네의 합 구하면 될거같은데??
    # 시간 오래 걸릴것 같으니까 합이 주어진 예산 M 넘어가면 break하기
    # lst가 비어있으면 result = 0
    result = 0                      # 결과값 저장해줄 변수
    if lst:                         # lst가 비어있지 않을때만 실행
        n = len(lst)
        for i in range(1<<n):
            tmp = 0                 # 현재 구하고 있는 부분집합의 합 저장해줄 변수 tmp
            for j in range(n):
                if i & (1<<j):      # i의 j번 비트가 0이 아니면 : 부분집합의 원소
                    tmp += lst[j]
                    # tmp가 예산 넘어가면 다음 부분집합 구하는걸로 넘어가기
                    if tmp > M:
                        break
            # tmp가 예산을 초과하지 않으면 tmp랑 result 비교해서 더 큰 값 저장
            if tmp <= M:
                if result < tmp:
                    result = tmp

    print(f'#{tc} {result}')

