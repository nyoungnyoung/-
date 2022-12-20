hexa = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
code = {'211': 0, '221': 1, '122': 2, '411': 3, '132': 4, '231': 5, '114': 6, '312': 7, '213': 8, '112': 9}

N, M = map(int, input().split())
for i in range(N):
    # 1줄씩 입력 받을건데, 해당 줄에 0만 있지 않으면 코드 포함된거!
    line = input()
    tmp = ''
    if line != '0' * M:
        for j in range(M):
            tmp += hexa[line[j]]
    print(tmp)