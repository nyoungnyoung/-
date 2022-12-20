from collections import deque
import sys

# 최소 이동횟수 구하는 거니까 bfs이용
def bfs(n):
    queue = deque([n])

now = 100
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
broke = list(map(int, sys.stdin.readline().split()))
visited = 
