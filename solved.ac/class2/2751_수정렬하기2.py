import sys

N = int(sys.stdin.readline())
lst = [0] * 2000002
for n in range(N):
    lst[int(sys.stdin.readline()) + 1000000] += 1

for i in range(2000002):
    if lst[i] != 0:
        for j in range(lst[i]):
            print(i - 1000000)
