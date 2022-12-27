# 위쪽 N극(빨간색) / 아래쪽 S극(파란색)
# 1(빨강) : N극 / 2(파랑) : S극 / 0 : 비어 있음
# 1번은 아래쪽으로 갈려고 함 / 2번은 위쪽으로 갈려고 함
# 진행방향에 다른 색깔이 없으면 사라짐
# 다른 색을 만나면 쌓임!
# 만약에 이케 세로줄을 하나씩 검사를하는데
# 세로줄에 1번이든 2번이든 하나만 있으면 얘네는 떨어져
# 중간에 빨강파랑이 만나는게 한개라도 있으면 같은색들은 쌓임
# 빨강파랑 개수를 세면 됨!
import sys
sys.stdin = open('magnetic_input.txt', 'r')


for tc in range(1, 11):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        lst = []
        for j in range(N):
            if table[j][i] == 1 or table[j][i] == 2:    # 빨간색이거나 파란색이면 리스트에 집어넣기
                lst.append(table[j][i])
        if len(lst) > 1:
            for k in range(len(lst) - 1):
                if lst[k] == 1 and lst[k+1] == 2:
                    cnt += 1
    print(f'#{tc} {cnt}')
