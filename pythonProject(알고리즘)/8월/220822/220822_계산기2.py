def to_post(data):
    # 중위표기식 data를 읽어서 후위표기식 문자열로 반환하는 함수
    # 피연산자이면 result에 더하기
    # 연산자이면, stack push
    # 단, 나보다 우선순위가 높거나 같은애들은 다 빼고 push
    isp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    icp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3}
    stack = []
    result = ''
    for i in range(len(data)):
        if data[i] in '+-*/()':
            if not stack:                   # 스택이 비어있으면
                stack.append(data[i])
            else:
                # ')' : 얘는 스택에 안들어감 vs 나머지
                if data[i] == ')':
                    # 여는 괄호가 나올때 까지 pop하면서 연산자 출력, 여는괄호는 버림
                    while stack[-1] != '(':
                        result += stack.pop()
                    stack.pop()     # 여는괄호 버리기(while문 끝나면 여는괄호 만난거니까)
                else:               # '+-*/(' 인 경우
                    # stack에 나보다 우선순위가 높거나 같은 애가 있으면 pop해서 빼버리고 들어감
                    # 아니라면 그냥 stack에 쌓아주면 됨
                    while stack and isp[stack[-1]] >= icp[data[i]]:      # stack의 top에 있는 게 나보다 작아지기 전까지 반복
                        result += stack.pop()
                    stack.append(data[i])       # while문 끝나면 내가 들어가면 됨!
        else:
            result += data[i]
    while stack:    # stack이 비어있지 않으면 stack에 남아있는 연산자들 모조리 꺼내서 붙혀 줘야 함
        result += stack.pop()
    return result


# 이제 후위 표기식을 계산하는 함수 작성하면 됨
def calculate(data):
    # 피연산자 : 일단 스택에 냅다 쌓음
    # 연산자 : 스택에서 두개 꺼내서 계산 후 결과 스택에 다시 넣기(나중에 들어간게 연산자 오른쪽에 와야함)
    stack = []
    for i in range(len(data)):
        if data[i] in '+-*/()':         # 연산자
            num2 = stack.pop()
            num1 = stack.pop()
            if data[i] == '+':
                stack.append(num1 + num2)
            elif data[i] == '-':
                stack.append(num1 - num2)
            elif data[i] == '*':
                stack.append(num1 * num2)
            elif data[i] == '/':
                stack.append(num1 // num2)
        else:                           # 피연산자
            stack.append(int(data[i]))
    return stack.pop()

for tc in range(1, 11):
    L = int(input())
    data = input()
    print(f'#{tc} {calculate(to_post(data))}')

