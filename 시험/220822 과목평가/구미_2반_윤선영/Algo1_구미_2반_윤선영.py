T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    Ai, Aj, Bi, Bj = map(int, input().split())      # 좌측상단 행 열 번호 Ai, Aj / 우측하단 행 열 번호 Bi, Bj 할당
    arr = [list(map(int, input().split())) for _ in range(N)]   # list comprehension 이용 N * N 마당 높이 입력받기
    # 일단 [Ai, Aj]부터 [Bi, Bj]까지 영역 돌면서 해당 영역의 평균값 구해야 함!
    sum_num = 0                         # 평균값 구하기 위해 영역의 합 저장할 변수 선언
    cnt = 0                             # 영역 내 땅의 수 세기 위한 변수 선언
    for i in range(Ai, Bi + 1):         # 행
        for j in range(Aj, Bj + 1):     # 열
            sum_num += arr[i][j]        # sum_num에 해당 영역의 높이 계속해서 더해주기
            cnt += 1                    # cnt에 +1
    # for문 다 돌고나면 sum_num에 영역 내 모든 땅들의 합이, cnt에 영역 내 땅의 수가 저장되어 있음
    # 이제 sum_num를 cnt로 나누어주면 평균값 구할 수 있음
    aver = sum_num // cnt
    # 평균값 구했으니 평탄화 작업 시작! 아까랑 똑같은 영역을 순회하면서,
    # 해당 칸의 숫자가 aver보다 작으면 두 수의 차만큼 높이를 올리고
    # aver보다 크면 두수의 차만큼 높이를 낮추고, 같으면 아무작업도 하지 않아야함
    # aver보다 작거나 같은 경우 : result += | arr[i][j] - aver |
    # 같은경우 : continue
    result = 0                                  # 평탄화 작업 횟수 저장하는 변수
    for i in range(Ai, Bi+1):                   # 행
        for j in range(Aj, Bj+1):               # 열
            if arr[i][j] < aver:                # 칸의 숫자가 aver보다 작으면
                result += (aver - arr[i][j])    # result에 aver - 칸의 숫자 더해주기
            elif arr[i][j] > aver:              # 칸의 숫자가 aver보다 크면
                result += (arr[i][j] - aver)    # result에 칸의 숫자 - aver 더해주기
    print(f'#{tc} {result}')                    # f-string 이용, 출력 형식 맞추기


