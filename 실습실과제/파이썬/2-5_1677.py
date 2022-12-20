crops = [('고구마', 3000), ('감자', 2000), ('옥수수', 4500), ('토란', 1300)]
price = []
for i in range(len(crops)):
    price.append(crops[i][1])

for j in range(len(crops)):
    if crops[j][1] == max(price):
        print(crops[j][0])
