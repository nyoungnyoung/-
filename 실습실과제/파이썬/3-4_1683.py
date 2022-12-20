blood_types = ['A', 'A', 'O', 'B', 'A', 'O',
               'AB', 'O', 'A', 'B', 'O', 'B', 'AB']

count = {}
for i in blood_types:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
print(count)
