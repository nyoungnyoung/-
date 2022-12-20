# idx번째 행에서 열 하나 선택해서 더하기 해 줄 예정
def arr_sum(idx, sum_num):      # dfs함수 만들기(idx : 시작 행)
    global min_sum
    # 시간 줄이기(이미 정답이 아님)
    if sum_num > min_sum:
        return

    if idx == N:               # idx가 arr의 모든 행을 돌았다는 뜻
        if min_sum > sum_num:
            min_sum = sum_num
        return

    for i in range(N):
        if visited[i] == 0:  # i번째 열에 접근한 적이 없다면
            visited[i] = 1
            arr_sum(idx + 1, sum_num + arr[idx][i])     # 재귀호출, 누적합에 arr[idx][i]
            # 사용 끝난 i, 방문했다는 표시 없애주어야 함
            visited[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N       # 방문한 열 확인해 줄 리스트 생성
    min_sum = 1000
    arr_sum(0, 0)
    print(f'#{tc} {min_sum}')