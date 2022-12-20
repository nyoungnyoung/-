import sys
N = int(sys.stdin.readline())
lst = []
for _ in range(N):
    lst += [list(map(int, sys.stdin.readline().split()))]
lst.sort()
for i in lst:
    print(*i)