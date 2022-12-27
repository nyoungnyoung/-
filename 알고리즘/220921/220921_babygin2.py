'''
5
123123
124567
333444
444456
123444
'''
T = int(input())
for tc in range(1, T+1):
    card = int(input())
    c = [0] * 12    # 인덱스가 9일때 도 run/tri 검사 할 수 있도록 10, 11 인덱스까지 만드는거!

    # count배열 만들기
    i = 0
    while i < 6:
        c[card%10] += 1
        card //= 10
        i += 1

    # baby-gin 판단
    tri = run = 0
    i = 1
    while i < 10:
        if c[i] >= 3:
            c[i] -= 3
            tri += 1
            continue
        if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1:
            c[i] -= 1
            c[i+1] -= 1
            c[i+2] -= 1
            run += 1
            continue        # 같은 자리에서 또 런이 시작될 수 있으니까 넘어가지말고 같은자리에서 한번 더 체크해봐~!
        i += 1
    if run + tri == 2:
        print(f'#{tc} Baby Gin')
    else:
        print(f'#{tc} Lose')
