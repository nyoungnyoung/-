T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    pattern = [list(map(int, input().split())) for _ in range(3)]
    # 0 ~ N - 2 행 / 0 ~ N - 2 열 돌면서, 해당칸으로부터 3 * 3 배열 확인(di, dj 이용)
    result = 0                          # 패턴 개수 저장할 변수 선언
    for i in range(N - 2):              # 시작칸 행
        for j in range(N - 2):          # 시작칸 열
            cnt = 0                     # 일치하는 칸수 확인할 변수 선언
            for di in range(3):         # 시작칸으로부터 di행만큼 움직이며 확인
                for dj in range(3):     # 시작칸으로부터 dj열만큼 움직이며 확인
                    # arr[i + di][j + dj] 와 pattern[di][dj] 가 같은지 확인!
                    if arr[i + di][j + dj] == pattern[di][dj]:
                        cnt += 1        # 일치 하면 cnt += 1
            if cnt == 9:                # for문 다 돌고 나서 cnt가 9이면
                result += 1             # 해당 칸으로부터 시작된 3 * 3 배열이 주어진 패턴과 똑같은 것! 결과에 +1
    print(f'#{tc} {result}')            # f-string 이용해 출력 형식 맞춰 결과 출력
