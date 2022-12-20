C = int(input())
for i in range(C):
    lst = list(map(int, input().split()))
    average = sum(lst[1:]) / lst[0]
    cnt = 0
    for j in lst[1:]:
        if j > average:
            cnt += 1
    print(f'{cnt/lst[0]*100:.3f}%')
