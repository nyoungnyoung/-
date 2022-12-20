import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))
count = {}
for i in lst:
    if i not in count:
        count[i] = 1
    else:
        count[i] += 1
for i in range(len(card)):
    card[i] = count.get(card[i], 0)
print(*card)
