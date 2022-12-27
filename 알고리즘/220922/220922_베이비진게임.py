def babygin(p):
    # tri 점검
    for j in range(10):
        if p[j] == 3:
            return True     # 승리
    # run 점검
    for k in range(8):      # 7까지 점검
        if p[k] and p[k+1] and p[k+2]:
            return True
    return False


T = int(input())
for tc in range(1, T + 1):
    card = list(map(int, input().split()))
    p1 = [0] * 10
    p2 = [0] * 10
    winner = 0
    for i in range(len(card)):
        if not i % 2:   # 짝수면
            p1[card[i]] += 1
            if babygin(p1):
                winner = 1
                break
        else:           # 홀수면면
            p2[card[i]] += 1
            if babygin(p2):
                winner = 2
                break
    print(f'#{tc} {winner}')
