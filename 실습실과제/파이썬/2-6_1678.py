orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'
orders_list = orders.split(',')
print(f"총 {len(orders_list)}잔의 주문이 들어왔습니다.")
print(sorted(set(orders_list), reverse=True))
