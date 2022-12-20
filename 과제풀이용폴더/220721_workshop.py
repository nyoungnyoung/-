# 1번
# def measure(N):
#     m_list = ''
#     for i in range(1, N+1):
#         if N % i == 0:
#             m_list += str(i) + ' '
#     return m_list


# print(measure(10))    # 1 2 5 10


# 2번
# def list_sum(lst):
#     sum_num = 0
#     for i in lst:  # lst 길이만큼 반복
#         sum_num += i
#     return sum_num


# print(list_sum([1,2,3,4,5]))


# 3번
# def dict_list_sum(info):
#     sum_age = 0
#     for i in info:
#         sum_age += i.get('age')  # i.get('age')로 'age'의 value값 가져오기
#     return sum_age


# print(dict_list_sum([{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}]))


# 4번
# def all_list_sum(lst_2):
#     sum_list = 0
#     for i in lst_2:
#         for j in i:
#             sum_list += j
#     return sum_list


# print(all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]))


# 5번
# def get_secret_word(word_lst):
#     word_chr = ''
#     for i in word_lst:
#         word_chr += chr(i)
#     return word_chr


# print(get_secret_word([83, 115, 65, 102, 89]))


# 6번
# def get_secret_number(str):
#     sum_ord = 0
#     for i in str:
#         sum_ord += ord(i)
#     return sum_ord


# print(get_secret_number('happy'))


# 7번
def get_strong_word(a, b):
    sum_ord_a = 0
    sum_ord_b = 0
    for i in a:
        sum_ord_a += ord(i)
    for j in b:
        sum_ord_b += ord(j)
    if sum_ord_a > sum_ord_b:
        return a
    elif sum_ord_a < sum_ord_b:
        return b
    else:
        return a, b


print(get_strong_word('z', 'a'))
print(get_strong_word('delilah', 'dixon'))
