import sys
sys.stdin = open('전기자동차충전소_input.txt', 'r')


# def charge(data):



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * 31 for _ in range(31)]
    for n in range(N):
        x, y, d = map(int, input().split())
    print(f'#{tc}')
