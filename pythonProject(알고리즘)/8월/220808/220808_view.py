import sys
sys.stdin = open('view_input.txt', 'r')

for t in range(1, 11):
    n = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    for i in range(2, n-2):
        max_val = 0
        for j in range(i-2, i+3):       # 좌/우 2칸 내에 나보다 높은 빌딩 x : 조망권 확보
            if j == i:                 # 나는 빼고 최댓값 찾기
                continue
            if max_val < lst[j]:     # 최대값 max_val 에 저장
                max_val = lst[j]
        if max_val < lst[i]:            # 최대값 < 나 : 조망권 확보
            cnt += lst[i] - max_val
    print(f'# {t} {cnt}')
