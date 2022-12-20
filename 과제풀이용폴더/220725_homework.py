# 1번
def count_vowels(word):
    vowels = 'aeiou'
    count = 0
    for n in vowels:
        if n in word:
            count += 1
    return count


print(count_vowels('apple'))

# 3번


def only_square_area(list_1, list_2):
    square_list = []
    for i in list_1:
        if i in list_2:
            square_list.append(i * i)
    return square_list


print(only_square_area([32, 55, 63], [13, 32, 40, 55]))
