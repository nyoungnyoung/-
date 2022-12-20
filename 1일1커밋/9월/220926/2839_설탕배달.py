import sys
N = int(sys.stdin.readline())
cnt = 0
while N >= 0:
    if N % 5 == 0:  # N이 5의 배수면
        cnt += N // 5
        print(cnt)
        break
    N -= 3
    cnt += 1
else:
    print(-1)
