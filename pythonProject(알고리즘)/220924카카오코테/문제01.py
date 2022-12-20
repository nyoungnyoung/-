# 개인정보 n 개 : 1 ~ n번
# 약관별 개인정보 유효기간 정해져있고, 유효기간 이후 파기해야함
# today : 오늘날짜 문자열 (YYYY.MM.DD)
# terms : 약관과 유효기간을 담은 1차원 문자열 리스트 ['약관종류 유효기간']
# 약관종류 : A ~ Z / 유효기간 : 1 ~ 100(달)
# privacies : 개인정보의 수집일자와 약관종류 나타내는 1차원 문자열리스트
            # ['날짜 약관종류', '날짜 약관종류]

def solution(today, terms, privacies):
    answer = []
    terms_dict = {}
    today_y, today_m, today_d = map(int, today.split('.'))
    # terms 돌면서 약관종류 / 유효기간 분리해서 dict에 담자
    for i in range(len(terms)):
        terms_name, terms_date = terms[i].split()
        terms_dict[terms_name] = int(terms_date) * 28
    # privacies 돌면서 날짜랑 약관 확인하고 today날짜에서 약관 날짜 빼주기, 약관에 따라 유효기간 지났는지 확인
    for i in range(len(privacies)):
        privacies_date, privacies_terms = privacies[i].split()
        privacies_y , privacies_m, privacies_d = map(int, privacies_date.split('.'))
        y = (today_y - privacies_y) * 12 * 28
        m = (today_m - privacies_m) * 28
        d = today_d - privacies_d
        # 유효기간 지나면 answer에다가 i+1 추가
        if terms_dict[privacies_terms] <= y + m + d:
            answer.append(i+1)
    return answer


a = '2022.05.19'
b = ['A 6', 'B 12', 'C 3']
c = ['2021.05.02 A', '2021.07.01 B', '2022.02.19 C', '2022.02.20 C']\
solution(a, b, c)

