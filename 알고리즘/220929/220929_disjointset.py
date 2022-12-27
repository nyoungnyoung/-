# 서로소 집합
# 서로 같은 집합인지 아닌지 확인하기 위해 대표자 개념을 가짐
# 각 노드는 부모를 가지는데, 노드 스스로가 부모이면 집합의 대표.
N = 10                  # 최대 노드 번호
parent = [x for x in range(0, N+1)]    # 인덱스에 해당하는 번호를 가지는 노드의 부모를 저장하는 배열 (parent[1] : 1번노드의 부모)
# 0번부터 10번까지의 노드를 만드는데, 스스로가 부모가 되도록 만듬!(makeset 함수 기능을 그냥 여기서 해결해버림)

# 인자로 받은 노드의 대표자 반환
def find_set(x):
    # 재귀
    # if x == parent[x]:
    #     return x
    # else:
    #     return find_set(parent[x])

    # 반복문(교수님은 얘가 더 보기 깔끔한것같다고 하심)
    while x != parent[x]:
        x = parent[x]
    return x

# 인자로 받은 두 노드의 집합을 합치기(대표자의 번호를 똑같이 만들어주기)
def union(x, y):
    # x의 대표자를 y의 대표자로 만들기
    # y의 대표자의 부모를 x의 대표자로 만들면 됨
    parent[find_set(y)] = find_set(x)

# 인자로 받은 두 노드가 같은 집합이면 True, 아니면 False반환 -> 서로소집합을 이용해서 그냥 임의로 만든 함수
def check_same_set(x, y):
    if find_set(x) == find_set(y):
        return True
    return False



union(1, 2)
union(4, 5)
union(1, 4)
print(parent)
print(check_same_set(1, 5))


