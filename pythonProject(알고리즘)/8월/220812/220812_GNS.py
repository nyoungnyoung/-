import sys
sys.stdin = open('GNS_input.txt', 'r')
T = int(input())
num_lst = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
for tc in range(1, T+1):
    num, num_len = input().split()
    num_len = int(num_len)
    lst = input().split()
    # 선택정렬
    # min_idx 만들어서 min_idx랑 자리 바꿔주기.. 근데 이게 숫자를 어떻게 비교하지?
    for i in range(int(num_len)-1):
        # min_num 초기값은 lst의 첫번재 원소(ex.TWO)
        # min_num_idx 초기값은 lst의 첫번째 원소(예를들어 ZRO)의 lst 인덱스(ex.0) 
        min_num = lst[i]
        min_num_idx = lst.index(min_num)
        for j in range(i, int(num_len)):
            # min_num의 num_lst 내 인덱스가 lst[j]의 num_lst 내 인덱스보다 크거나 같으면
            if num_lst.index(min_num) >= num_lst.index(lst[j]):
                min_num = lst[j]
                min_num_idx = j
        lst[i], lst[min_num_idx] = lst[min_num_idx], lst[i]
    print(f'#{tc}')
    print(*lst)