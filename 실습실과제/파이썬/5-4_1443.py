# 같은 숫자가 한 개 있거나 두 개 들어있는 리스트
# 숫자가 한 개만 있는 요소들의 합을 구하는 sum_of_repeat_number()
# ex) [4,4,7,8,10,4] -> 한번씩만 나오는 7,8,10의 합 25 출력

def sum_of_repeat_number(lst):
    result = 0
    for i in lst:
        if lst.count(i) == 1:
            result += i
    return result

print(sum_of_repeat_number([4,4,7,8,10,4]))