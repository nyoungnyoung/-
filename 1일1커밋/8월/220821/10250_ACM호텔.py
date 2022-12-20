# 호텔 정문으로부터 걸어서 가장 짧은 거리에 있는 방 선호
# 호텔은 각 층에 W개의 방이 있는 H층 건물, 엘리베이터는 가장 왼쪽에 있음
# 호텔 정문은 일층 엘리베이터 바로 앞에 있음
# 엘리베이터 타고 이동하는 거리는 신경 쓰지 않음
# 걷는 거리가 같을 때에는 아래층 방을 더 선호함
# N번째로 도착한 손님에게 배정될 방 번호 계산하여 출력
import sys
T = int(sys.stdin.readline())
for tc in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    floor = N % H
    room = (N // H) + 1
    if N % H == 0:      # N이 H의 배수인 경우
        floor = H
        room -= 1
    result = floor * 100 + room
    print(result)