import sys
N = int(sys.stdin.readline())
lst = []
for _ in range(N):
    lst.append(int(sys.stdin.readline().strip()))
lst.sort()
dic = {}
for i in range(len(lst)):
    if lst[i] not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
print(dic)
a = round(sum(lst)/N, 1)
b = lst[N//2 + 1]

d = lst[-1] - lst[0]