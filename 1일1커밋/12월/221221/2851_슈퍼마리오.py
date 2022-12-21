import sys

lst = [int(sys.stdin.readline().strip()) for _ in range(10)]
score = 0
for i in lst:
    # 일단 버섯 먹기(score += i)
    score += i
    # score가 100을 넘어가면 버섯을 먹기 전 숫자와 먹었을 때 숫자 중
    # 100에 더 가까운 숫자 구하기
    if score >= 100:
        tmp = score - i
        if 100 - tmp < score - 100:
            score -= i
        break
print(score)