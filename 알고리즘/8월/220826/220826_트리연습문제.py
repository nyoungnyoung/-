"""
V : 정점 개수 / V-1 : 간선 개수(두 정점으로 표기 됨, 부모 자식 순서)
# 13
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
# [0, 1, 2, 3, 4, 0, 5, 6, 7, 0, 0, 0, 8, 9, 10, 11, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 0]
"""
V = int(input())
H = 4
tree = [0]*(2**(H+1))
tree[1] = 1
data = list(map(int, input().split()))
for i in range(V-1):
    parent = tree.index(data[i*2])  # 부모노드 인덱스
    if tree[parent*2]:
        tree[parent*2+1] = data[i*2+1]  # 자식노드 인덱스(부모노드 인덱스 *2 or 부모노드인덱스 *2 + 1)
    else:
        tree[parent*2] = data[i*2+1]
print(tree)


# 루트노드에서 시작해서 순회하는 함수
# 루트 노드를 인자로 받음(노드의 인덱스를 인자로 받음)
# n : 현재노드


def preorder(n):
    if n >= 2**(H+1) or tree[n] == 0:
        return
    """
    # n이 tree의 인덱스를 벗어나면 순회 멈춰!
    # n이 가리키는 인덱스의 값이 0이면, 노드가 없음! 순회 멈춰!
    """
    print(tree[n], end=' ')
    preorder(n*2)
    # print(tree[n], end=' ')   중위순회
    preorder(n*2+1)
    # print(tree[n], end=' ')   후위순회


preorder(1)






# 내가 짜다만거

# def dfs(T):

# V = int(input())
# lst = list(map(int, input().split()))
# tree = [[] for _ in range(V + 1)]
# for i in range(0, len(lst), 2):
#     a, b = lst[i], lst[i+1]
#     tree[a].append(b)

