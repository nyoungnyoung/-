import sys
sys.stdin = open('달란트2_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, T = map(int, input().split())
    dalent = [0] * T
    for i in range(N):
        dalent[i % T] += 1
    result = 1
    for j in dalent:
        result *= j
    print(f'#{tc} {result}')
