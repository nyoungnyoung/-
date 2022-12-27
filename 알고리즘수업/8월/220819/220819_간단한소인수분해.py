def factorization(n):
    d = [2, 3, 5, 7, 11]
    lst = [0] * 5
    while n > 1:                # n이 1이 될때까지 반복
        for i in range(len(d)):
            if n % d[i] == 0:   # n이 d의 [i]로 나누어떨어지면
                n /= d[i]       # n = n // d[i]
                lst[i] += 1
    print(*lst)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc}', end=' ')
    factorization(N)


# 쇠막대기 자르기