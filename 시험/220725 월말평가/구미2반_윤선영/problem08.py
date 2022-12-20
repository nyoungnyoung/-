def filter(item_type, inventory):
    new_list = []
    for i in range(len(inventory)):  # 인벤토리를 길이만큼 순회하면서
        # 인벤토리의 i번째 딕셔너리(인덱스)의 'type'값이 item_type과 같으면
        if inventory[i]['type'] == item_type:
            new_list.append(inventory[i])
    return new_list


# print(filter('weapon', [
#     {'id': 1, 'name': 'Elder Wand', 'type': 'weapon', 'grade': 'legend'},
#     {'id': 2, 'name': 'Healing Potion', 'type': 'potion', 'grade': 'normal'},
#     {'id': 3, 'name': 'Steel Helmet', 'type': 'armor', 'grade': 'rare'},
#     {'id': 4, 'name': 'Long Sword', 'type': 'weapon', 'grade': 'normal'},
# ]))
