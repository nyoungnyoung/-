def is_triangle(lst):
    lst.sort()
    a, b, c = lst[0], lst[1], lst[2]
    if c**2 == a**2 + b**2:
        return 'right'
    else:
        return 'wrong'


while True:
    t_lst = list(map(int, input().split()))
    if t_lst == [0, 0, 0]:
        break
    print(is_triangle(t_lst))
