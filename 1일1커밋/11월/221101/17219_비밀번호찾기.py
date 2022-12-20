import sys
N, M = map(int, sys.stdin.readline().split())
lst = {}
for _ in range(N):
    A, B = sys.stdin.readline().split()
    lst[A] = B
for _ in range(M):
    search = sys.stdin.readline().strip()
    print(lst[search])
