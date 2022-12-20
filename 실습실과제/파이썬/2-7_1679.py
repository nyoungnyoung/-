orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'
orders_list = orders.split(',')
orders_sorted = sorted(orders_list)
menu = sorted(set(orders_list))
isice = []
count_ice = 0

for i in range(len(orders_list)):   # order_list의 길이만큼 반복
    isice.append(orders_list[i][:3])

for j in range(len(orders_list)):
    if isice[j] == '아이스':
        count_ice += 1

print(f'아이스 음료는 {count_ice}개 입니다.')

# 전체 주문 수만큼 반복하면서 음료가 바뀌면 -> 해당 음료 개수를 세서 count에 저장
count = []
for k in range(len(orders_sorted)):
    if orders_sorted[k] != orders_sorted[k - 1]:
        count.append(orders_sorted.count(orders_sorted[k]))

for l in range(len(menu)):                 # 메뉴 개수만큼 반복해서 출력 count_orders 출력
    print(f'{menu[l]} : {count[l]}')
