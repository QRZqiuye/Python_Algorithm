# 이진 탐색 트리 구현 (탐색, 삽입, 삭제)

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # 탐색 알고리즘
    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    # 삽입 알고리즘
    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

    # 삭제 알고리즘
    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node

        # 탐색
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # 경우 1: 자식이 없는 경우
            if node.left is None and node.right is None:
                return None
            # 경우 2: 자식이 하나인 경우
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # 경우 3: 자식이 두 개인 경우
            else:
                successor = self._min_value_node(node.right)
                node.key = successor.key
                node.right = self._delete(node.right, successor.key)
        return node

    # 최소값 노드 찾기 (삭제 시 사용)
    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    # 중위 순회 (오름차순 출력)
    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)


# 테스트 코드
bst = BST()

# 삽입
for value in [50, 30, 70, 20, 40, 60, 80]:
    bst.insert(value)

print("중위 순회 결과 (삽입 후):", bst.inorder())

# 탐색
node = bst.search(40)
print("탐색 40:", "찾음" if node else "없음")

node = bst.search(90)
print("탐색 90:", "찾음" if node else "없음")

# 삭제
bst.delete(20)  # 단말 노드 삭제
print("20 삭제 후:", bst.inorder())

bst.delete(30)  # 자식이 하나인 노드 삭제
print("30 삭제 후:", bst.inorder())

bst.delete(50)  # 자식이 두 개인 노드 삭제
print("50 삭제 후:", bst.inorder())
