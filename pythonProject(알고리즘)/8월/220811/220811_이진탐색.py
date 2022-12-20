# 전체쪽수 : P / A목표 : Pa / B목표 : Pb
# 구간의 왼쪽 : l / 구간의 중간 : c(l+r//2) / 구간의 끝 : r
# 이진탐색 게임에서 이긴 사람이 누구인지 출력, 비긴경우 0 출력

# A랑 B 둘다 이진탐색 해야하니까 차라리 함수를 하나 만들자
def search(p, l, c, r):
    cnt = 0
    while l <= r:       # 시작점이 끝점보다 커지면 끝내기
        c = (l+r)//2
        if c == p:      # 탐색성공
            cnt += 1
            return cnt
        elif c > p:     # c 오른쪽 구간 버리기
            cnt += 1
            r = c
        else:           # c 왼쪽 구간 버리기
            cnt += 1
            l = c
    return cnt

T = int(input())
for tc in range(1, T+1):
    result = 0              # 이긴사람 저장하는 변수
    P, Pa, Pb = map(int, input().split())
    # 이진탐색 시작          # 몇번 반복할지 모르니까 일단 while문 돌려보자
    # A
    la, ra, lb, rb = 1, P, 1, P
    ca = (la + ra) // 2
    cb = (lb + rb) // 2
    A = search(Pa, la, ca, ra)
    B = search(Pb, lb, cb, rb)
    if A < B:   # A가 이김
        result = 'A'
    elif A > B: # B가 이김
        result = 'B'
    else:
        result = 0

    print(f'#{tc} {result}')