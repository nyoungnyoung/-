T = int(input())

for tc in range(1, T+1):
    N = input()
    M = input()
    n, m = len(N), len(M)
    cnt = False
    # M의 길이에서 N의 길이 뺀거에 +1 해준만큼 비교 해야함!
    for i in range(m - n + 1):
        for j in range(n):
            if M[i+j] != N[j]:
                break
        else:
            cnt = True
    print(f'#{tc} {int(cnt)}')

