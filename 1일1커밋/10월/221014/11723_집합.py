import sys
M = int(sys.stdin.readline())
lst = set()
for _ in range(M):
    order = sys.stdin.readline().split()

    # order 길이가 1이면 명령어가 all/empty
    if len(order) == 1:
        if order[0] == 'all':
            lst = set(i for i in range(1, 21))
        else:
            lst = set()

    else:
        oper, num = order[0], int(order[1])
        if oper == 'add':
            lst.add(num)
        elif oper == 'remove':
            lst.discard(num)
        elif oper == 'check':
            if num in lst:
                print(1)
            else:
                print(0)
        elif oper == 'toggle':
            if num in lst:
                lst.discard(num)
            else:
                lst.add(num)
