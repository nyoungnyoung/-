from itertools import combinations
import sys
N, K = map(int, sys.stdin.readline().split())
print(len(list(combinations(range(N), K))))