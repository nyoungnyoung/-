import sys
N = int(sys.stdin.readline())
lst = []
for n in range(N):
    lst.append(sys.stdin.readline().rstrip())
# 중복 제거를 위해 set 활용
lst = list(set(lst))
# 사전 순으로 정렬
lst.sort()
# sort의 key값에 len을 지정해줌으로써, 단어 길이순으로 정렬
lst.sort(key=len)
for w in lst:
    print(w)
