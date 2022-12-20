n, m = map(int,input().split())
for i in range(m):      # m만큼 반복해서 출력(세로)
    for j in range(n):  # n만큼 반복해서 출력(가로)
        print('*',end='') # * 출력
    print()

# 교수님 코드
# 가로 = n / 세로 = m 이면
# 별 n개 찍는 걸 m번 반복해야함
n, m = map(int,input().split())
for i in range(m):
    print('*' * n)
    