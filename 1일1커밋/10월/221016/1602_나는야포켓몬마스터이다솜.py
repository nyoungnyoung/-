import sys
N, M = map(int, sys.stdin.readline().split())
poketmon_name = {}
poketmon_num = {}
num = 1

for _ in range(N):
    name = sys.stdin.readline().strip()
    poketmon_name[num] = name
    poketmon_num[name] = num
    num += 1

for i in range(M):
    info = sys.stdin.readline().strip()
    if info.isdigit():
        print(poketmon_name[int(info)])
    else:
        print(poketmon_num[info])

