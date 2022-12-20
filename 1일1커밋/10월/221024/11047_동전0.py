N, K = map(int, input().split())
cnt = 0
money = [int(input()) for _ in range(N)]
for j in range(N-1, -1, -1):
    if money[j] <= K:
        cnt += K // money[j]
        K %= money[j]
    if K == 0:
        break
print(cnt)