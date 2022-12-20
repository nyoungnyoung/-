import sys
sys.stdin = open('sum_input.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    max_list = []
    # 최대행의 합 max_si
    max_si = 0
    for i in range(100):    # 행마다 돌면서 행의 합 si구하기
        si = 0
        for j in range(100):
            si += arr[i][j]
        if max_si < si:     # max_si보다 si가 크면
            max_si = si
    max_list.append(max_si)

    # 최대열의 합 max_sj
    max_sj = 0
    for j in range(100):    # 열먼저 돌면서 열의합 sj구하기
        sj = 0
        for i in range(100):
            sj += arr[i][j]
        if max_sj < sj:
            max_sj = sj
    max_list.append(max_sj)

    for i in range(100):
        sl = 0
        sl += arr[i][i]
        sr = 0
        sr += arr[i][99-i]
    max_list.append(sl)
    max_list.append(sr)

    result = 0
    for m in range(len(max_list)):
        if result <= max_list[m]:
            result = max_list[m]

    print(f'#{tc} {result}')


# 처음 코드
# for tc in range(1, 11):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(100)]
#     max_list = []
#     # 최대행의 합 max_si
#     max_si = 0
#     for i in range(100):    # 행마다 돌면서 행의 합 si구하기
#         si = 0
#         for j in range(100):
#             si += arr[i][j]
#         if max_si < si:     # max_si보다 si가 크면
#             max_si = si
#     max_list.append(max_si)

#     # 최대열의 합 max_sj
#     max_sj = 0
#     for j in range(100):    # 열먼저 돌면서 열의합 sj구하기
#         sj = 0
#         for i in range(100):
#             sj += arr[i][j]
#         if max_sj < sj:
#             max_sj = sj
#     max_list.append(max_sj)

#     # 왼쪽위->오른쪽아래로 향하는 대각선 합 sl 중 최대값 max_sl
#     max_sl = 0
#     for i in range(100):
#         sl = 0
#         sl += arr[i][i]
#         if max_sl < sl:
#             max_sl = sl
#     max_list.append(max_sl)

#     # 오른쪽위->왼쪽아래로 향하는 대각선 합 sr
#     max_sr = 0
#     for i in range(100):
#         sr = 0
#         sr += arr[i][99-i]
#         if max_sr < sr:
#             max_sr = sr
#     max_list.append(max_sr)

#     result = 0
#     for m in range(len(max_list)):
#         if result <= max_list[m]:
#             result = max_list[m]

#     print(f'#{tc} {result}')
