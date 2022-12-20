from itertools import combinations


def solution(orders, course):
    lst = []
    for idx in orders:
        for n in course:
            course_lst = list(combinations(list(map(int, idx))), n)
            print(course_lst)
    answer = []
    return course_lst
