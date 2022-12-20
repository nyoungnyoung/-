T = int(input())
for tc in range(1, T + 1):
    cost = list(map(int, input().split()))
    plan = [0] + list(map(int, input().split()))
    money = [0] * 13                            # 가격 저장해줄 리스트
    for i in range(1, 13):
        # 1일 이용권 cost[0] * 이용일 vs 1달 이용권 cost[1]
        money[i] = min(cost[0] * plan[i], cost[1]) + money[i-1]
        # 3월부터는 money[i]에 저장된 값 vs money[i-3] + 3달 이용권 cost[2] 비교
        if i >= 3:
            money[i] = min(money[i], money[i-3] + cost[2])
    # 반복문 다 돌고나면 money[12]에 저장된 값 vs 1년 이용권 cost[3] 비교
    result = min(money[12], cost[3])
    print(f'#{tc} {result}')
