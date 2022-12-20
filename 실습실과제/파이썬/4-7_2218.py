words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

# eat tea ate
# tan nat
# bat

result = {}
for i in words:
    a = ''.join(sorted(i))        # sorted(i) = ['a', 'e', 't']
    result[a] = result.get(a,[]) + [a]
print(list(result.values()))