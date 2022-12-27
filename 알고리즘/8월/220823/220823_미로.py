# 0 : 통로 / 1 : 벽 / 2 : 출발 / 3 도착
# 맨 밑 줄 2 -> 맨 윗 줄 3
# 도착 가능 : 1 / 도착 불가능 : 0
def maze_run(arr):
    # 위 / 오른쪽 / 아래 / 왼쪽 델타 선언
    di = [-1, 0, 1, 0]     # 행
    dj = [0, 1, 0, -1]     # 열
    for i in range(N):
        for j in range(N):


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input().strip())) for _ in range(N)]
    print(maze)