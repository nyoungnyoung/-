import sys
sys.stdin = open('단순2진암호코드_input.txt', 'r')


num = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    code = ''
    # 행마다 입력값인 line 확인해서 1이 들어가있으면 code 포함되어 있는 줄
    # line의 뒤쪽부터 확인해서 1이 있으면 j-55부터 j+1까지를 코드에 저장
    for i in range(N):
        line = input()
        if '1' in line:
            for j in range(M-1, -1, -1):
                if line[j] == '1':
                    code = line[j-55:j+1]
                    break
    code_lst = []
    for i in range(0, 56, 7):
        code_lst.append(num[code[i:i+7]])
    # 올바른 code인지 판단 하기
    result = 0
    for i in range(8):
        if (i + 1) % 2:     # 짝수자리이면
            result += code_lst[i] * 3
        else:               # 홀수자리이면
            result += code_lst[i]
    if result % 10 == 0:     # 옳은 암호이면
        result = sum(code_lst)
    else:                   # 옳은 암호 아니면
        result = 0

    print(f'#{tc} {result}')
