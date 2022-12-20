# 입력으로 N 개의 점수가 주어졌을 때, 중간값을 출력하라.
# N은 항상 홀수/ 9 <= N <= 199
# 크기 순으로 배열 했을 때 전체의 중앙에 위치하는 수치
N = int(input())
score = sorted(list(map(int, input().split())))
print(score[N // 2])
