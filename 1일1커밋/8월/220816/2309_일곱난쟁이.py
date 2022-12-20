# combinations 이용

from itertools import combinations
lst = []
for _ in range(9):
    lst.append(int(input()))
for i in combinations(lst, 7):
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break
