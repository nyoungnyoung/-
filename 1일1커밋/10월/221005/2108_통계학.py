from collections import Counter
import sys

N = int(sys.stdin.readline())
lst = []
for n in range(N):
    lst.append(int(sys.stdin.readline()))
lst.sort()

# 산술평균
print(round(sum(lst)/N))

# 중앙값
print(lst[N//2])

# 최빈값 (여러개면 최빈값 중 두번째로 작은값 출력)
# 최빈값이 여러개면 tmp 리스트 내에 (값, 개수) 형태로 저장됨
tmp = Counter(lst).most_common()
if len(tmp) >= 2 and tmp[0][1] == tmp[1][1]:  # 최빈값 2개이상이면
    print(tmp[1][0])                      # 두번째로 작은 값 출력
else:                       # 아니면
    print(tmp[0][0])        # 제일 작은 값 출력

# 범위 : 최댓값 - 최솟값
print(max(lst)-min(lst))