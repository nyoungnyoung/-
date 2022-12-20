import sys
N = int(sys.stdin.readline())
# 0의 개수 세어줄 변수
cnt = 0
while N > 0:
    cnt += N//5
    N //= 5
print(cnt)