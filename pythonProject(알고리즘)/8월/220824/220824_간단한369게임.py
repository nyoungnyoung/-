def game(n):
    for i in range(1, n+1):
        cnt = 0
        for j in str(i):
            if int(j) % 3 == 0 and j != '0':
                cnt += 1
        if cnt == 0:
            print(i, end=' ')
        else:
            print('-' * cnt, end=' ')


N = int(input())
game(N)
