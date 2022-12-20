import sys

K, N = map(int, sys.stdin.readline().split())
lst = []
for _ in range(K):
    lst.append(int(sys.stdin.readline()))

left, right = 1, max(lst)


# 이분탐색 하면 될것같음!
while left <= right:            # left가 right보다 커질때까지 반복
    mid = (left + right) // 2   # 랜선길이
    cnt = 0                     # 랜선 길이
    for i in lst:
        cnt += i // mid

    # for문 다 돌고나서 cnt와 N 비교해보기
    if cnt < N:                 # cnt < N이면 mid-1을 right로 설정
        right = mid - 1
    else:                       # 아니면 mid+1을 left로 설정
        left = mid + 1

print(right)


