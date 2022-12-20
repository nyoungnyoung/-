import sys
sys.stdin = open('암호코드스캔_input.txt', 'r')

# 16 진수 -> 2진수 변경 딕셔너리 / 암호코드의 0, 1, 0 ,1 비율로 나타낸 숫자 딕셔너리
hexa = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
code = {(2, 1, 1): 0, (2, 2, 1): 1, (1, 2, 2): 2, (4, 1, 1): 3, (1, 3, 2): 4, (2, 3, 1): 5, (1, 1, 4): 6, (3, 1, 2): 7, (2, 1, 3): 8, (1, 1, 2): 9}

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    result = 0          # 결과 저장해 줄 변수 선언
    for i in range(N):
        # 1줄씩 입력 받을건데, 해당 줄에 0만 있지 않으면 코드 포함된거!
        line = input()
        tmp = ''                # 2진수 코드 잠깐 저장해둘 변수
        if line != '0' * M:
            for j in range(M):  # line의 모든 원소들을 2진수로 변경후 tmp에 붙혀주기
                tmp += hexa[line[j]]

        # 그러면 이제 tmp를 뒤쪽부터 돌아보면서 0과 1의 개수 번갈아가며 세보자
        password = []       # 변환완료한 암호코드 저장해 줄 리스트
        for idx in range(len(tmp)-1, -1, -1):
            for _ in range(8):
                if tmp[idx] == '1':         # 암호코드 여기부터 시작된다!
                    # cnt_1 : 0 개수 / cnt_2 : 1 개수 / cnt_3 : 0 개수 / / cnt_4 : 1 개수
                    cnt_1 = cnt_2 = cnt_3 = cnt_4 = 0
                    # 뒤에서부터 1 개수 세기
                    while tmp[idx] == '1':
                        cnt_4 += 1
                    # 0 개수 세기
                    while tmp[idx] == '0':
                        cnt_3 += 1
                    # 1 개수 세기
                    while tmp[idx] == '1':
                        cnt_2 += 1
                    # 이제 cnt들의 비율가지고 cnt_1 구해주기
                    r = min(cnt_2, cnt_3, cnt_4)
                    cnt_1 = 7 * r - (cnt_2 + cnt_3 + cnt_4)
                    idx -= cnt_1
                    cnt_1 //= r
                    cnt_2 //= r
                    cnt_3 //= r
                    cnt_4 //= r
                    password.insert(0, code[(cnt_2, cnt_3, cnt_4)])
                    # password = [7, 5, 7, 5, 5, 0, 2, 7]
                    # 이런식으로 숫자 8개 얻고 나면(password길이 8이 되면)
                    # 정상적인 코드인지 확인 후, 정상적이면 sum(password)
                    # result에 더해주고, password 초기화

                # 정상적?
                odd = password[1] + password[3] + password[5]
                even = password[0] + password[2] + password[4] + password[6]
                if (odd * 3 + even + password[7]) % 10 == 0:
                    result += sum(password)
                password = []

    print(f'#{tc} {result}')
