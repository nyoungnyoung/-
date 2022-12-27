def Forth(data):
    stack = []
    for i in range(len(data)):
        if data[i] == '.' and len(stack) == 1:         # i번째 요소가 '.'이면서 stack에 남은 숫자가 1개일 때 pop해서 return
            return stack.pop()
        if data[i] == '.' and len(stack) != 1:         # i번째 요소가 '.'인데 stack에 남은 숫자가 1개가 아닐 때는 error
            return 'error'
        if data[i] in '+-*/':           # i번째 요소가 연산자일 경우
            try:                        # try - except 구문으로 에러처리
                num2 = stack.pop()      # 숫자 2개를 pop할 수 없을 경우 에러 발생
                num1 = stack.pop()
            except:
                return 'error'
            if data[i] == '+':
                stack.append(num1 + num2)
            elif data[i] == '-':
                stack.append(num1 - num2)
            elif data[i] == '*':
                stack.append(num1 * num2)
            else:
                stack.append(num1 // num2)
        else:                           # i번째 요소가 숫자일 경우
            stack.append(int(data[i]))


T = int(input())
for tc in range(1, T + 1):
    lst = input().split()
    result = Forth(lst)
    print(f'#{tc} {result}')