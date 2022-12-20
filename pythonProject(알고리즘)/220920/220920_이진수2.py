T = int(input())
for tc in range(1, T + 1):
    N = float(input())
    result = ''
    i = 1
    while N:
        if N < 2 ** (-i):
            result += '0'
        else:
            result += '1'
            N -= 2 ** (-i)
        if len(result) > 12:
            result = 'overflow'
            break
        i += 1

    print(f'#{tc} {result}')

