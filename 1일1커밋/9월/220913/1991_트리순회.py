# 전위순회
def preorder(n):
    if n != '.':
        print(n, end='')
        preorder(tree[n][0])
        preorder(tree[n][1])
# 중위순회
def inorder(n):
    if n != '.':
        inorder(tree[n][0])
        print(n, end='')
        inorder(tree[n][1])
# 후위순회
def postorder(n):
    if n != '.':
        postorder(tree[n][0])
        postorder(tree[n][1])
        print(n, end='')


import sys
N = int(sys.stdin.readline().strip())
tree = dict()
for _ in range(N):
    V, L, R = map(str, sys.stdin.readline().split())
    tree[V] = L, R

preorder('A')
print()
inorder('A')
print()
postorder('A')
