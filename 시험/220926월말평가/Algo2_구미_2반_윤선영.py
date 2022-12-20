# 전위 순회
def preorder(n):
    if n:
        pre_lst.append(n)
        preorder(c1[n])
        preorder(c2[n])


# 중위 순회
def inorder(n):
    if n:
        inorder(c1[n])
        in_lst.append(n)
        inorder(c2[n])


# 후위 순회
def postorder(n):
    if n:
        postorder(c1[n])
        postorder(c2[n])
        post_lst.append(n)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 왼쪽 자식 노드 c1 / 오른쪽 자식 노드 c2
    c1 = [0] * (N + 1)
    c2 = [0] * (N + 1)
    # 트리 상태 저장부터 해보자..!
    for i in range(1, N + 1):
        if c1[i] == 0 and 2 * i <= N:
            c1[i] = 2 * i
        if c2[i] == 0 and 2 * i + 1 <= N:
            c2[i] = 2 * i + 1

    # 순회별 방문순서 저장해 줄 리스트
    pre_lst = []
    in_lst = []
    post_lst = []

    # 순회하기
    preorder(1)
    inorder(1)
    postorder(1)

    # 새로운 트리 상태 저장해줄 리스트
    tree = [0] * N
    for i in range(N):
        tree[i] = max(pre_lst[i], in_lst[i], post_lst[i])

    print(f'#{tc}', end=' ')
    print(*tree)
