T = int(input())
for tc in range(1, T+1):
    # N*N 크기의 글자판(arr)에서 길이가 M인 회문을 찾아 출력
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    # 가로 먼저 검사해보자!
    for i in range(N):
        # 시작점 잡아주기
        for j in range(N - M + 1):
            word = ''
            # 회문 검사(arr[i]번째 행에 j+k번째 요소와 j+M-k번째 요소가 같으면
            # for문 계속 돌리고 같지 않으면 다음 시작점으로 가서 반복하기!
            for k in range(M):
                if arr[i][j+k] == arr[i][j+M-1-k]:
                    word += arr[i][j+k]
                else:
                    break
            else:
                print(f'#{tc} {word}')

    # 세로는 i랑 j만 바꿔주면 됨!
    for i in range(N):
        for j in range(N - M + 1):
            word = ''
            for k in range(M):
                if arr[j+k][i] == arr[j+M-1-k][i]:
                    word += arr[j+k][i]
                else:
                    break
            else:
                print(f'#{tc} {word}')
