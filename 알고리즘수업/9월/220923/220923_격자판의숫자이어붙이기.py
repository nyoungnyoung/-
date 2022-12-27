def dfs(x, y, tmp):                         # tmp : 만들 수 있는 숫자를 문자열로 저장해 줄 변수
    tmp += arr[x][y]                        # 현재 위치에 적혀있는 수(문자열)를 tmp에 더해주자
    if len(tmp) == 7:                       # tmp 길이가 7이 되면
        # if tmp not in num:                  # tmp가 num안에 없을때
            num.append(tmp)                 # tmp를 num리스트 안에 추가해주고
            return
    # 상 / 하 / 좌 / 우 델타
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < 4 and 0 <= ny < 4:     # nx, ny가 범위 내에 있으면
            dfs(nx, ny, tmp)                     # nx, ny에서 동일한 작업 수행해보자~!


T = int(input())
for tc in range(1, T + 1):
    arr = [list(map(str, input().split())) for _ in range(4)]
    num = []
    for i in range(4):
        for j in range(4):
            dfs(i, j, '')
    result = len(set(num))
    print(f'#{tc} {result}')
