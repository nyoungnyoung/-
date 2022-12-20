# 1번
def get_dict_avg(scores):
    return sum(scores.values()) / len(scores)


print(get_dict_avg({
    'python': 80,
    'web': 83,
    'algorithm': 90,
    'django': 89,
}))

# 2번


def count_blood(blood_list):
    blood_dictionary = {}
    for i in blood_list:
        if i in blood_dictionary:
            blood_dictionary[i] += 1
        else:
            blood_dictionary[i] = 1
    return blood_dictionary


print(count_blood([
    'A', 'B', 'A', 'O', 'AB', 'AB',
    'O', 'A', 'B', 'O', 'B', 'AB',
]))
