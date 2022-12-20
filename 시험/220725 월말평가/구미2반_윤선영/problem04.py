# [신규 생성 아이디, 기존유저 아이디, 기존유저 아이디, ...]
# 신규 생성 아이디가 기존 아이디와 중복되면 True
# 아니면 False 반환하는 check_duplicate_id 함수
# 반복문 돌면서 리스트의 0번째 인덱스(신규생성아이디)와
# 일치하는 인덱스가 있는지 확인

def check_duplicate_id(id_list):
    for i in range(1, len(id_list)):
        if id_list[0] == id_list[i]:
            return True
        else:
            return False


# print(check_duplicate_id(['dfweqe', 'adjkle', 'jjklwejlk', 'wjeklj']))
