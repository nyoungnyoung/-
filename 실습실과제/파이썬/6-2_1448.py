grain_lst = [('고구마', 3000), ('감자', 2000), ('옥수수', 4500), ('토란', 1300)]
price = []
for i in range(len(grain_lst)):
    price.append(grain_lst[i][1])

for j in range(len(grain_lst)):
    if grain_lst[j][1] == max(price):
        print(grain_lst[j][0])
