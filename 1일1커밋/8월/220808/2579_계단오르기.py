import sys
lst = []
dp = []
n = int(sys.stdin.readline())

for i in range(n):
    s = int(sys.stdin.readline())
    lst.append(s)       # lst에 계단 높이 저장
    if i == 0:
        dp.append(lst[0])
    elif i == 1:
        dp.append(lst[0] + lst[1])
    elif i == 2:
        dp.append(max(lst[0] + lst[2], lst[1] + lst[2]))
    else:
        dp.append(max(dp[i-3] + lst[i-1] + lst[i], dp[i-2] + lst[i]))

print(dp[n-1])




