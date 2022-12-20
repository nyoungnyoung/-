def duplicated_letters(str):
    result = []
    for i in str:
        if str.count(i) != 1 and i not in result:
            result.append(i)
    return result

print(duplicated_letters('apple'))
print(duplicated_letters('banana'))

def low_and_up(str):
    result = ''
    for i in str:
        if str.index(i) % 2 == 0:
            result += i.lower()
        elif str.index(i) % 2 == 1:
            result += i.upper()
    return result

print(low_and_up('apple'))
print(low_and_up('Banana'))
print(low_and_up('lower'))
print(low_and_up('LlLle'))


def lonely(lst):
    result = []
    for i in range(len(lst)):
        if i == 0:
            result.append(lst[i])
        elif lst[i] != result[-1]:
            result.append(lst[i])
    return result

print(lonely([1, 1, 3, 3, 0, 1, 1]))
print(lonely([4, 4, 4, 3, 3]))

