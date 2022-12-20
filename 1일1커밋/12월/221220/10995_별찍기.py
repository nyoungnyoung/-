import sys

N = int(sys.stdin.readline().split())
for i in range(N):
    # N이 홀수일 때
    if N % 2 != 0:
        print('* ' * N)
    # N이 짝수일 때
    else:
        print()