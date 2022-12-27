import sys
sys.stdin = open('스도쿠_input.txt', 'r')

def sudoku(arr):
    # 가로
    for i in range(9):
        lst = [0] * 10
        for j in range(9):
            if lst[arr[i][j]] == 0:
                lst[arr[i][j]] = 1
            else:
                return False
    # 세로
    for i in range(9):
        lst_2 = [0] * 10
        for j in range(9):
            if lst_2[arr[j][i]] == 0:
                lst_2[arr[j][i]] = 1
            else:
                return False
    # 격자
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            lst_3 = [0] * 10
            for di in range(3):
                for dj in range(3):
                    if lst_3[arr[i + di][j + dj]] == 0:
                        lst_3[arr[i + di][j + dj]] = 1
                    else:
                        return False
    return True

T = int(input())
for tc in range(1, T + 1):
    sudo = [list(map(int, input().split())) for _ in range(9)]    # 숫자 그대로 인덱스로 쓰기 위해 각 행 앞에 0 추가
    result = sudoku(sudo)
    print(f'#{tc} {int(result)}')
