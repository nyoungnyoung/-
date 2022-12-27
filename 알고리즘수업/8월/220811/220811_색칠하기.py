T = int(input())

for tc in range(1, T+1):
    N = int(input())
    note = [[0] * 10 for _ in range(10)]
    cnt = 0
    for n in range(N):
        sr, sc, er, ec, color = map(int, input().split()) 
        if color == 1:               # 색상이 빨강이면
            for i in range(sr, er+1):
                for j in range(sc, ec+1):
                    if note[i][j] == 0:
                        note[i][j] = 'red'
                    else:
                        note[i][j] = 'violet'
        elif color ==2:               # 색상이 파랑이면
            for i in range(sr, er+1):
                for j in range(sc, ec+1):
                    if note[i][j] == 0:
                        note[i][j] = 'blue'
                    else:
                        note[i][j] = 'violet'
    for i in range(10):
        for j in range(10):
            if note[i][j] == 'violet':
                cnt += 1
    print(f'#{tc} {cnt}')