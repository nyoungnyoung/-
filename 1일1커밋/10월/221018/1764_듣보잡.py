import sys
N, M = map(int, sys.stdin.readline().split())
l_people = set()
s_people = set()
for _ in range(N):
    l_people.add(sys.stdin.readline().strip())

for _ in range(M):
    s_people.add(sys.stdin.readline().strip())

lst = []
for i in l_people:
    if i in s_people:
        lst.append(i)
lst.sort()
print(len(lst))
for j in lst:
    print(j)