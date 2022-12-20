from itertools import permutations
from collections import deque


def solution(expression):
    # 우선순위 정해주기(순열 이용)
    priority_lst = list(permutations(['+', '-', '*'], 3))
    answer = 0

    for idx in priority_lst:
        # 일단 expression split먼저 해주기(연산자와 피연산자로 나누어줘야함!)
        # 처음에는 이 부분을 for문 밖에서 해줬는데, 그러면 하나의 우선순위에
        # 따라 연산이 끝난 후에 lst 초기화를 해 주지 못해 잘못된 답이 나왔음
        num = ''
        lst = deque()
        for i in expression:
            # i가 숫자면 num에 계속 더해주다가
            if i.isdigit():
                num += i
            # 연산자를 만나면 num에 저장된 값을 lst에 넣어주고 연산자도 넣어주기
            else:
                lst.append(num)
                lst.append(i)
                num = ''
        # 마지막 숫자도 lst에 넣어줘야함!
        lst.append(num)

        for op in idx:
            calculate = []
            # lst에서 숫자나 연산자 뽑아와서 우선순위에 맞는 연산자가 나오면 계산해주기
            # 해당하는 연산자가 아니면 calculate에 push! lst가 빌때까지 while문 반복!
            # -> while문 탈출하면 answer이랑 calculate안에 남은 숫자의 절댓값 비교해서 큰 값 저장, 다음 우선순위의 연산자로 while문 돌기
            while len(lst) != 0:
                n = lst.popleft()
                if n == op:
                    # eval(str) : str형태의 계산식 결과 return
                    tmp = str(eval(calculate.pop() + n + lst.popleft()))
                    calculate.append(tmp)
                else:
                    calculate.append(n)
            lst = deque(calculate)

        result = abs(int(calculate.pop()))
        if answer <= result:
            answer = result

    return answer

