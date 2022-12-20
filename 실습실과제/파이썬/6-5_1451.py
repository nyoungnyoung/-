# 반복문 사용
def sum_of_digit(num):
    sum_num = 0
    for i in str(num):
        sum_num += int(i)
    return sum_num

print(sum_of_digit(123))

# 반복문 사용x
def sum_of_digit2(num):
    return sum(list(map(int,str(num))))

print(sum_of_digit2(456))