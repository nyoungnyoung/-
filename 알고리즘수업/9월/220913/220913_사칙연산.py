# 후위 순회 사용해야 밑에서부터 계산 가능!
def postorder(n):
    if tree[n]:
        if type(tree[n]) == int:   # n번 노드의 값이 숫자면
            return tree[n]
        else:                       # 아니면 : 연산자
            A, B = postorder(left[n]), postorder(right[n])
            if tree[n] == '+':
                return A + B
            elif tree[n] == '-':
                return A - B
            elif tree[n] == '*':
                return A * B
            elif tree[n] == '/':
                return A // B


for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N + 1)        # 트리 상태
    left = [0] * (N + 1)        # 왼쪽 자식 노드
    right = [0] * (N + 1)       # 오른쪽 자식 노드
    for _ in range(N):
        # 트리 저장부터 해줘야함!
        node, *val = input().split()
        node = int(node)
        if val[0] in '+-*/':
            tree[node], left[node], right[node] = val[0], int(val[1]), int(val[2])
        else:
            tree[node] = int(val[0])
    print(tree)
    print(f'#{tc} {postorder(1)}')
