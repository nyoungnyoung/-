N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
cnt = []        # 바꿔야할 칸 개수들 저장해 줄 리스트

# board를 8 * 8 배열로 쪼개서 확인해보기! 시작인덱스 i, j
for i in range(N - 7):
    for j in range(M - 7):
        # 첫 칸이 흰색일 때 / 첫 칸이 검정색일 때
        cnt_w = 0
        cnt_b = 0
        for x in range(i, i + 8):
            for y in range(j, j + 8):
                # x, y의 합이 짝수일 경우, 시작점의 색과 같아야 함!
                # 홀수일 경우 시작점의 색과 달라야함
                if (x + y) % 2 == 0:    # 짝수일경우
                    if board[x][y] != 'W':
                        cnt_w += 1
                    if board[x][y] != 'B':
                        cnt_b += 1
                else:                   # 홀수일경우
                    if board[x][y] != 'B':
                        cnt_w += 1
                    if board[x][y] != 'W':
                        cnt_b += 1
        cnt.append(min(cnt_w, cnt_b))
print(min(cnt))