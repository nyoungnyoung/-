def post(data):     # 중위표기법 -> 후위표기법 바꾸는 함수
    icp = {'+': 1, '*': 2, '(': 3}      # stack에 들어갈때 우선순위
    isp = {'+': 1, '*': 2, '(': 0}
    stack = []
    result = ''
    for i in range(len(data)):
        if data[i] not in '+*()':        # i번째 원소가 숫자면
            result += data[i]            # result에 해당 원소 더해주기
        else:                            # i번째 원소가 연산자면
            if data[i] == '(':
                pass



def calculate(data):        # 후위표기법 계산하는 함수
    pass


for tc in range(1, 11):
    L = int(input())
    lst = input()
    print(f'#{tc}')