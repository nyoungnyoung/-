import sys
sys.stdin = open('flatter_input.txt', 'r')

# 최댓값, 최솟값 구하는 함수


def max_min(lst):
    max_val = lst[0]
    min_val = lst[0]
    max_idx = 0
    min_idx = 0
    for i in range(len(lst)):
        if max_val <= lst[i]:
            max_val = lst[i]
            max_idx = i
        if min_val >= lst[i]:
            min_val = lst[i]
            min_idx = i
    return max_idx, min_idx


for tc in range(1, 11):
    dump = int(input())
    box = list(map(int, input().split()))
    for i in range(dump):   # dump 제한횟수만큼 dump 시행
        max_i, min_i = max_min(box)     # max_idx와 min_idx 구해서 변수에 할당
        if box[max_i] - box[min_i] == 0 or box[max_i] - box[min_i] == 1:
            break
        box[max_i] -= 1
        box[min_i] += 1

    max_box, min_box = max_min(box)     # 덤프 완료한 이후의 max_min값 구해서 변수에 할당
    print(f'#{tc} {box[max_box]-box[min_box]}')
