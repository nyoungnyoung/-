# 스테이크   50,000
# + VAT     7,500
# 총계 ₩    57,500

steak = 50000
vat = int(50000 * 0.15)
price = steak + vat
steak = format(steak, ',')
vat = format(vat, ',')
price = format(price, ',')

print(f'스테이크\t{steak}')
print(f'+ VAT\t\t{vat}')
print(f'총계 ₩\t\t{price}')
