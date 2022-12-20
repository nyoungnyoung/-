words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

# eat tea ate
# tan nat
# bat

def group_anagrams(lst):
    result = {}
    for i in lst:
        a = ''.join(sorted(i))      # sorted(i) = ['a', 'e', 't']
        result[a] = result.get(a,[]) + [i]

    return list(result.values())


print(group_anagrams(words))