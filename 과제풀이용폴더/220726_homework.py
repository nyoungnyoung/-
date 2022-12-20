# 1번
lst = [3, 6, 9, 10, 2, 8, 5]
print(lst)
print(sorted(lst))
print(lst)
print(lst.sort())
print(lst)

# 2번
cafe = ['starbucks']
cafe.append(['hollys'])
cafe.extend(['hollys'])
print(cafe)
cafe.append('twosome')
cafe.extend('twosome')
print(cafe)

# 3번
a = [1, 2, 3, 4, 5]
b = a
a[2] = 5
print(a)
print(b)
