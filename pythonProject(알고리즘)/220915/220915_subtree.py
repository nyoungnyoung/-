# 노드 개수 세기 위해 전위순회 함수 만들기
def preorder(v):
    global cnt
    if v:
        cnt += 1
        preorder(tree[0][v])
        preorder(tree[1][v])


# 이진트리에서 노드 N을 루트로하는 서브 트리에 속한 노드의 개수 출력
T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())
    lst = list(map(int, input().split()))
    # 부모 - 자식 노드 번호 쌍(E개) / 노드 개수 : E + 1 (노드 번호 그대로 인덱스 사용하기 위해 E+2)
    tree = [[0] * (E + 2) for _ in range(2)]
    # tree상태 입력받기
    for i in range(0, len(lst), 2):
        if tree[0][lst[i]] == 0:
            tree[0][lst[i]] = lst[i + 1]
        else:
            tree[1][lst[i]] = lst[i + 1]
    # N을 루트로 하는 서브트리 노드 개수 세기
    cnt = 0
    preorder(N)
    print(f'#{tc} {cnt}')