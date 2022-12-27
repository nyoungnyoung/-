class Node:
    def __init__(self, data):
        # 데이터를 저장하는 저장공간
        self.data = data
        # 왼쪽 / 오른쪽 자식 참조 변수
        self.left = None
        self.right = None

class MyTree:
    # 트리는 루트부터 탐색하기 때문에, 루트만 저장
    def __init__(self, data):
        self.root = Node(data)

    # 트리에 노드 추가
    def add_node(self, parent, child):
        # 부모노드 찾아온 다음에, 새로운 노드 만들어서 추가
        p_node = self.get_node(self.root, parent)        # 이부분 뭔가 이상함
        if p_node.left is None:
            p_node.left = Node(child)
        else:
            p_node.right = Node(child)

    # val에 해당하는 노드 반환하는 메서드
    # 루트부터 시작해서 val에 해당하는 노드가 있는지 탐색
    def get_node(self, current, val):
        # None이라면 노드가 아님!
        if current is None:
            return None
        # None이 아니라면 데이터 확인해서 내가 찾고있는 노드번호랑 같은지 판단
        if current.data == val:
            return current
        result1 = self.get_node(current.left, val)
        result2 = self.get_node(current.right, val)
        if result1 is not None:
            return result1
        if result2 is not None:
            return result2
        return None

    def print_nodes(self):
        self.preorder(self.root)

    def preorder(self, node):
        if node is None:
            return
        print(node.data, end=' ')
        self.preorder(node.left)
        self.preorder(node.right)

        pass

    def inorder(self):
        pass

    def postorder(self):
        pass


V = int(input())
data = list(map(int, input().split()))
tree = MyTree(1)
for i in range(V-1):
    # data[i*2] 부모노드, data[i*2+1] 자식노드
    tree.add_node(data[i*2], data[i*2+1])

tree.print_nodes()


