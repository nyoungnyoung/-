def charge(n):
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    need = [0] * 8
    # 주석처리된 부분은 런타임에러 뜸
    # i = 0
    # while n != 0:       # 주어진 돈이 0이 되면 반복 종료
    #     if n - money[i] < 0:    # 주어진 돈에서 money의 i번째 요소를 뺀 값이 음수이면
    #         i += 1              # i에 +1 (한단위 낮은 단위의 돈을 빼주기 위해)
    #     else:                   # 아니면
    #         n -= money[i]       # 주어진 돈에서 money의 i번째 요소 빼주고
    #         need[i] += 1        # need의 i번째 요소에 +1 (필요한 돈 개수 세기 위해)
    # return need                 # 반복문 종료 시 need값 반환
    for i in range(len(money)):
        if n // money[i] != 0:          # money의 i번째 요소로 n을 나눈 몫이 0이 아니면
            need[i] = n // money[i]     # need[i]에 그 몫을 넣어주고
            n %= money[i]               # n을 나머지로 바꿔주기
    return need


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc}')
    print(*charge(N))

