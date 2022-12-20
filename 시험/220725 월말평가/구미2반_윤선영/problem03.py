# 딕셔너리 형태로 user_data 주어짐
# 입력된 정보에서 id를 문자열형태로 반환하는 get_user_id함수
# 딕셔너리 key값 이용해 value값 추출하기 dict['key']
# 문자열 형태로 반드시 바꿔줄것!

def get_user_id(user_data):
    return(str(user_data['id']))


# print(get_user_id({'id': 'adjfkl', 'password': 'wjrkjglw123'}))
