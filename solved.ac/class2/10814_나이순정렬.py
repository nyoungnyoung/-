import sys
N = int(sys.stdin.readline())
lst = [sys.stdin.readline().split() for _ in range(N)]
lst.sort(key=lambda x: int(x[0]))
for idx in lst:
    print(*idx)

# 처음 풀이
'''
N = int(input())
lst = {}
for _ in range(N):
    age, name = input().split()
    age = int(age)
    if age not in lst:
        lst[age] = [name]
    else:
        lst[age] += [name]
sorted_lst = sorted(lst.items())
for i in range(len(sorted_lst)):
    if len(sorted_lst[i][1]) == 1:
        print(sorted_lst[i][0], sorted_lst[i][1][0])
    else:
        for j in range(len(sorted_lst[i][1])):
            print(sorted_lst[i][0], sorted_lst[i][1][j])
'''