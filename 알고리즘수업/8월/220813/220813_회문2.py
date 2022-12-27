import sys
sys.stdin = open('회문2_input.txt', 'r')
for _ in range(10):
    T = int(input())
    arr = [input() for _ in range(100)]
    for M in range(2, 101):
        # 가로
        for i in range(100):
            for j in range(100 - M + 1):
                for k in range(M//2):
                    if arr[i][j + k] != arr[i][j + M - 1 - k]:
                        break
                else:
                    result = M

        # 세로는 i랑 j만 바꿔주면 됨!
        for i in range(100):
            for j in range(100 - M + 1):
                for k in range(M//2):
                    if arr[j + k][i] != arr[j + M - 1 - k][i]:
                        break
                else:
                    result = M
    print(f'#{T} {result}')
