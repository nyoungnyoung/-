# 교재 p.39 - 41 바이너리 카운팅 이용 부분집합 생성방법
# 모든 부분집합을 만들 때 유용함!
# 그러면 얘를 재귀를 이용해서 만들면? 부분집합_재귀.py
arr = [3, 6, 7, 1, 5, 4]
n = len(arr)

for i in range(1<<n):       # i : 0 ~ 2**n - 1 / range(1, 1<<n) 하면 공집합 빼고 만들어짐
    for j in range(n):
        if i & (1<<j):      # i의 j번 비트가 0이 아니면 arr[j]가 부분집합의 원소가 됨
            print(arr[j], end=' ')
    print()
