import sys
sys.stdin = open('Ladder_input.txt', 'r')
for _ in range(1, 11):
    T = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    # delta 선언(위/왼/오)
    dx = [-1, 0, 0]
    dy = [0, -1, 1]
    # ladder 젤 아래쪽 행에서 2 있는 열(x_position) 찾기
    x_position = 0
    for i in range(100):
        if ladder[-1][i] == 2:
            x_position = i

    # 현재 위치(2가 있는 곳)
    x, y = 99, x_position
    while x > 0: # x가 0이 될때까지 반복(1번째줄까지)
        # 왼쪽 행에 1이 있으면 현재위치 0으로 바꿔준 후 왼쪽으로 이동
        if y > 0 and ladder[x][y-1] == 1:
            ladder[x][y] = 0
            x += dx[1]
            y += dy[1]
        # 오른쪽 행에 1이 있으면 현재위치 0으로 바꿔준 후 오른쪽으로 이동
        elif y < 99 and ladder[x][y+1] == 1:
            ladder[x][y] = 0
            x += dx[2]
            y += dy[2]
        # 둘다 아니면 현재 위치 0으로 바꿔주고 위로 이동
        else:
            ladder[x][y] = 0
            x += dx[0]
            y += dy[0]
    print(f'#{_} {y}')
    
    # 기본적으로 위로 이동하되,
    # 왼쪽/오른쪽 원소가 1이면 그쪽 방향으로 이동하는 것으로 변경한다.
    # 행의 끝(1번째 줄)에 도착하면 종료
 
   