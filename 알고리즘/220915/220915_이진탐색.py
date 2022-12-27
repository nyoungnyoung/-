# 이진탐색트리: 중위순회하면 오름차순 정렬됨
# 중위순회 함수 만들어두고 작업하는 위치에서 해당 노드에 숫자 넣으면 됨!

def inorder(v):
    global cnt, N
    if v <= N:
        inorder(2*v)        # 왼쪽 자식
        cnt += 1            # 노드에 넣어줄 숫자에 +1씩
        if tree[v] == 0:    # 해당 노드에 숫자가 안적혀있으면
            tree[v] = cnt   # cnt 적어주기!
        inorder(2*v+1)      # 오른쪽 자식

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    tree = [0] * 1001       # 1 <= N <= 1000 
    cnt = 0
    inorder(1)
    print(f'#{tc} {tree[1]} {tree[N//2]}')