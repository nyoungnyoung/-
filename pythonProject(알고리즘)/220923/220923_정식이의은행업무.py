'''
정식이의 은행업무 : 2, 3진수 둘다 한자리씩 바꿔가며 탐색하면 됨(완전탐색 문제)
장훈이의 높은 선반 : 최대한 낮은 높이로 탑을 쌓을거임! 주어진 높이보다 크거나 같은 탑 중에 최소값(부분집합? 이용해서 풀면될듯)
디저트카페 :
격자판의 숫자 이어붙이기 : 왔던곳 다시 이동 가능, 0으로 시작하는 수도 만들 수 있음, 격자판이 주어졌을 때 만들 수 있는 서로다른 일곱자리 수! (모든 경우 탐색하면서, 경우의 수를 줄여주는 방법 생각하는게 중요!)
미생물 격리 : 시뮬레이션 문제, 모든 경우를 다 해봐야 함. 그냥 이때까지 배운 내용 총 동원해서 어떻게든 풀면 됨
'''

T = int(input())
for tc in range(1, T + 1):
    bi = input()
    tri = input()
    bi_lst, tri_lst = [], []
    result = 0
    for i in range(len(bi)):
        binary = list(bi)
        if binary[i] == '0':
            binary[i] = '1'
            bi_lst.append(int(''.join(binary), 2))
        else:
            binary[i] = '0'
            bi_lst.append(int(''.join(binary), 2))
    for i in range(len(tri)):
        trit = list(tri)
        if trit[i] == '0':
            trit[i] = '1'
            tri_lst.append(int(''.join(trit), 3))
            trit[i] = '0'
            trit[i] = '2'
            tri_lst.append(int(''.join(trit), 3))
        if trit[i] == '1':
            trit[i] = '2'
            tri_lst.append(int(''.join(trit), 3))
            trit[i] = '1'
            trit[i] = '0'
            tri_lst.append(int(''.join(trit), 3))
        else:
            trit[i] = '0'
            tri_lst.append(int(''.join(trit), 3))
            trit[i] = '2'
            trit[i] = '1'
            tri_lst.append(int(''.join(trit), 3))
    for i in bi_lst:
        if i in tri_lst:
            result = i
            break
    print(f'#{tc} {result}')
