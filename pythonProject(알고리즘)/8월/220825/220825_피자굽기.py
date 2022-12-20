# 1번부터 M번까지 M개의 피자를 순서대로 넣는다.
# 피자는 1번자리에서만 넣거나 뺄 수 있다.
# 화덕을 한바퀴 돌고나면 녹지 않은 치즈의 양은 C//2로 줄어듬
# 치즈가 0이되면 화덕에서 꺼낸 후 그 자리에 남은 피자를 순서대로 넣는다.
# 가장 마지막에 남아있는 피자 번호를 알아내라
# (피자번호, 치즈양) >>> 화덕에 넣기

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())        # N : 화덕 크기 / M : 피자 개수
    C = list(map(int, input().split()))     # C : 치즈 양
    fire = []                               # 화덕(큐)
    for i in range(N):                      # 화덕 크기만큼
        fire.append([i + 1, C[i]])          # [피자 번호, 치즈 양] 추가하기

    j = 0
    while len(fire) != 1:                   # 화덕 안에 피자가 하나만 남을때까지 반복
        cheese = fire.pop(0)
        cheese[1] //= 2                     # cheese[1]에 치즈의 양 들어있음!
        if cheese[1] == 0:                  # 꺼내서 확인했을 때 0이면
            if j + N < M:                   # 아직 남은 피자가 있는지 확인해서
                fire.append([N + j + 1, C[N + j]])      # 새로운 피자 화덕에 넣기
                j += 1
        else:                               # 치즈가 아직 덜 녹았으면
            fire.append(cheese)             # 다시 화덕에 넣기

    result = fire[0][0]                     # 화덕안에 들어가있는 피자의 번호
    print(f'#{tc} {result}')



