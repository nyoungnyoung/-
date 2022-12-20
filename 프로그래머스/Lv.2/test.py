from itertools import combinations

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]

for idx in orders:
    for n in course:
        course_lst = list(combinations(idx, n))
        print(course_lst)