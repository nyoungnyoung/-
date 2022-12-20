T = int(input())

# 우 하 좌 상 순서로 움직이게 만드는 delta 만들기
# 0 : 오른쪽 / 1 : 아래쪽 / 2 : 왼쪽 / 3 : 위쪽 (4의 나머지 - % 4)
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    # 달팽이가 움직일 방향을 전하는 변수 d / 달팽이가 지나간 자리에 적어줄 숫자
    d = 0
    num = 1
    r, c = 0, 0     # 시작점 & 현재위치
    while num <= N * N:
        # 달팽이 움직이기
        # 근데, 만약에 움직이려는 칸으로 못가면 방향전환해주기
        arr[r][c] = num
        num += 1
        # 다음칸으로 이동, 내가 이동중인 방향으로 계속 이동
        r += dr[d]
        c += dc[d]
        if r < 0 or r >= N or c < 0 or c >= N or arr[r][c] != 0:  # 비정상 범위이거나 다른 숫자가 들어가있다면(!= 0d은 생략가능)
            r -= dr[d]
            c -= dc[d]
            # 방향전환과 동시에 다시 이동
            d = (d + 1) % 4  
            r += dr[d]
            c += dc[d]

    print(f'#{tc}')
    