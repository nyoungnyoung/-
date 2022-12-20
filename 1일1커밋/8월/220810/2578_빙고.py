import sys

# 일단 입력 받기!
# A : 철수 빙고판 2차원 list / B : 사회자가 부르는 수 list
A = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]
B = []
for lst in range(5):
    B.extend(list(map(int, sys.stdin.readline().split())))

# 빙고 판별 함수


def is_bingo(arr):
    bingo = 0
    # 행 확인
    for i in range(5):
        for j in range(5):
            # 같은 행 내에 0이 아닌게 하나라도 있으면 안됨
            if arr[i][j] != 0:
                break
        else:
            bingo += 1

    for i in range(5):
        for j in range(5):
            if arr[j][i] != 0:
                break
        else:
            bingo += 1

    for i in range(5):
        if arr[i][i] != 0:
            break
    else:
        bingo += 1

    for i in range(5):
        if arr[i][4-i] != 0:
            break
    else:
        bingo += 1

    return bingo


# B의 원소들 하나씩 돌면서 A에 있는 원소들이랑 비교, 같으면 0으로 바꾸기
cnt = 0
for b in B:
    cnt += 1
    for i in range(5):
        for j in range(5):
            if A[i][j] == b:
                A[i][j] = 0
            if is_bingo(A) >= 3:
                print(cnt)
                exit()
