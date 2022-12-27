# 왼쪽자식값+오른쪽자식값을 부모노드에다가 넣어주면 될듯?
def sum_tree(v):
    global N
    if v < N + 1:
        if tree[v] == 0:    # 노드에 값이 없는 경우
            tree[v] = sum_tree(2*v) + sum_tree(2*v+1)
        return tree[v]      # 노드에 값이 있으면 넘어가고
    else:                   # 노드번호가 범위를 넘어가면 0 리턴
        return 0


T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)
    for _ in range(M):
        node, num = map(int, input().split())
        tree[node] = num

    sum_tree(1)
    print(f'#{tc} {tree[L]}')
