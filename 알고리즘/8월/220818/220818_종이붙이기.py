T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    row = N // 10
    dp = [1, 3]
    if row < 3:
        result = dp[row - 1]
    else:
        for i in range(2, row):
            dp.append(dp[i - 1] + dp[i - 2] * 2)
        result = dp[row - 1]
    print(f'#{tc} {result}')
