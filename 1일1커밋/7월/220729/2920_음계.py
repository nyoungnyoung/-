# 1 2 3 4 5 6 7 8 : ascending
# 8 7 6 5 4 3 2 1 : descending
# else : mixed

num = input().split()  
if sorted(num) == num:   # sorted한 값이랑 num이랑 같으면 ascending
    print('ascending')
elif sorted(num, reverse= True) == num:     # 내림차순정렬한거랑 num이랑 같으면 descending
    print('descending')
else:
    print('mixed')