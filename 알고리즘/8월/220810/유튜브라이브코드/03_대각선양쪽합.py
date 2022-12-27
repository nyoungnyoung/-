# 대각선(i == j) 왼쪽아래(i > j)와 오른쪽위(i < j) 원소들의 합 중 더 큰 값은 얼마?
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

s1 = 0
s2 = 0
for i in range(N):
    for j in range(N):
        if i > j:
            s1 += arr[i][j]
        elif i < j:
            s2 += arr[i][j]

# 또 다른 방법? 와 천재들인가ㅋㅋㅋ
s1 = 0
s2 = 0
for i in range(N):
    for j in range(i+1, N):
        s2 = arr[i][j]
        s1 = arr[j][i]


# 반대 대각선의 경우에도 한번 생각해보기!
