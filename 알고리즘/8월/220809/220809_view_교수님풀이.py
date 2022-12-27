# 입력 받기
# input() >> 표준 입력(콘솔입력)으로, 문자열 한 줄 읽어오기
# 콘솔 >> 파일에서 읽어오도록 변경
import sys
sys.stdin = open('input.txt', 'r')      # r : 읽기 / w : 쓰기
# sys.stdin = open('output.txt', 'r')


for tc in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))
    # 문제 풀면 되는데..
    # 2 ~ N-3번 건물까지 조망권 확보된 세대
    result = 0
    for i in range(2, N-2):
        # 조망권 확보된 세대 계산하기
        # 양쪽 2칸에 있는 건물들 높이 확인하기
        # 제일 높은 건물 높이 찾고, 현재 건물이 주변 건물보다
        # 높으면 조망권이 확보되었으니 더해주기
        # i-2번 건물부터 i+2번 건물까지 제일 높은 건물 높이 구하기
        max_height = 0
        for j in range(i-2, i+3):
            if j == i:
                continue
            if buildings[j] > max_height:
                max_height = buildings[j]

        if max_height < buildings[i]:  # 조망권 확보된 세대가 있다는 뜻
            result += buildings[i] - max_height

        # 최대값 찾을 때는, 최대값 저장하는 변수의 초기값 = 최대한 작게
        # 최소값 찾을 때는, 변수의 초기값을 최대한 크게
        # max 쓸 수 있으면
        # max(buildings[i-2], buildings[i-1], buildings[i+1], buildings[i+2])
    print(f'#{tc} {result}')