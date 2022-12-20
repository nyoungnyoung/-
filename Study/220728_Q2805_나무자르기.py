n, m = map(int, input().split())
trees = list(map(int, input().split()))
first, last = 0, max(trees)

while first <= last:             # first가 last보다 작거나 같을 동안만 반복
    h = (first + last) // 2      # 중간값
    cnt = 0                      # 상근이가 가져간 나무
    for i in trees:              # trees를 돌면서
        if i > h:                # i(나무 높이)가 h보다 크면
            cnt += i - h         # 자른다! cnt에 더해주기
    if cnt >= m:                 # 가져간 나무가 목표치 m보다 크면
        first = h + 1            # first를 h보다 1 높게 설정
    else:                        # m보다 작거나 같으면
        last = h - 1             # last를 h보다 1 작게 설정
# first가 last보다 커지는 순간 반복 종료
print(last)
