'''
정점 번호 V : 1 ~ (E + 1)
<input>
간선 수
부모-자식 순
4
1 2 1 3 3 4 3 5
'''
# 루트 찾는 함수
def find_root(V):
    for i in range(1, V + 1):
        if par[i] == 0:     # 부모가 없으면 root
            return i

# 전위순회
def preorder(n):
    if n:
        print(n, end=' ')    # visit(n)
        preorder(c1[n])
        preorder(c2[n])

# 중위순회
def inorder(n):
    if n:
        inorder(c1[n])
        print(n, end=' ')  # visit(n)
        inorder(c2[n])

# 후위순회
def postorder(n):
    if n:
        postorder(c1[n])
        postorder(c2[n])
        print(n, end=' ')  # visit(n)


E = int(input())
lst = list(map(int, input().split()))
V = E + 1
# 부모를 인덱스로 자식 번호 저장
c1 = [0] * (V + 1)
c2 = [0] * (V + 1)
# 자식을 인덱스로 부모 번호 저장
par = [0] * (V + 1)

for i in range(E):
    p, c = lst[i*2], lst[i*2+1]
# for j in range(0, E*2, 2):
#   p, c = lst[j], lst[j+1]
    if c1[p] == 0:  # 아직 자식이 없으면
        c1[p] = c   # 자식 1로 저장
    else:
        c2[p] = c
    par[c] = p

# 루트 찾기
root = find_root(V)

preorder(root)
print()
inorder(root)
print()
postorder(root)
