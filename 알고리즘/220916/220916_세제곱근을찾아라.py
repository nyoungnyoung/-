T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # x에 임의의 수 1 넣어놓음!
    x = 1
    while True:
        num = x ** 3
        # x를 3제곱한 수가 N과 같아지면 멈춤
        if num == N:
            break
        if num > N:
            x = -1
            break
        if num < N:
            x += 1
    print(f'#{tc} {x}')
