from itertools import combinations

n, m = map(int, input().split())
card = list(map(int, input().split()))
sum_num = 0
for i in combinations(card, 3):
    if sum(i) <= m and sum_num < sum(i):
        sum_num = sum(i)

print(sum_num)
