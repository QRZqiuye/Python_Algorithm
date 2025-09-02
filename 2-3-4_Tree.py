class Node234:
    def __init__(self):
        self.keys = []      # 값들 (정렬된 상태 유지)
        self.children = []  # 자식 노드들

    def is_leaf(self):
        return len(self.children) == 0

    def is_full(self):
        return len(self.keys) == 3


class Tree234:
    def __init__(self):
        self.root = Node234()

    # 탐색 알고리즘
    def search(self, node, key):
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        if i < len(node.keys) and key == node.keys[i]:
            return True
        if node.is_leaf():
            return False
        return self.search(node.children[i], key)

    # 삽입 알고리즘
    def insert(self, key):
        root = self.root
        if root.is_full():  # 루트가 4-노드면 분할
            new_root = Node234()
            new_root.children.append(root)
            self.split(new_root, 0)
            self.root = new_root
        self._insert_non_full(self.root, key)

    def _insert_non_full(self, node, key):
        i = len(node.keys) - 1
        if node.is_leaf():
            node.keys.append(key)
            node.keys.sort()
        else:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if node.children[i].is_full():
                self.split(node, i)
                if key > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], key)

    def split(self, parent, i):
        node = parent.children[i]
        new_node = Node234()
        mid = node.keys[1]

        # 새 자식 분리
        new_node.keys = node.keys[2:]
        node.keys = node.keys[:1]

        if not node.is_leaf():
            new_node.children = node.children[2:]
            node.children = node.children[:2]

        parent.keys.insert(i, mid)
        parent.children.insert(i + 1, new_node)

    # 삭제 알고리즘 (단순 버전: 리프에서만 삭제, 내부 노드 삭제는 미구현)
    def delete(self, key):
        self._delete(self.root, key)

    def _delete(self, node, key):
        if key in node.keys:
            if node.is_leaf():
                node.keys.remove(key)
            else:
                print("내부 노드 삭제는 단순 버전에서 지원하지 않습니다.")
        else:
            i = 0
            while i < len(node.keys) and key > node.keys[i]:
                i += 1
            if node.is_leaf():
                return
            self._delete(node.children[i], key)

    # 중위 순회
    def inorder(self, node, result=None):
        if result is None:
            result = []
        if node.is_leaf():
            result.extend(node.keys)
        else:
            for i in range(len(node.keys)):
                self.inorder(node.children[i], result)
                result.append(node.keys[i])
            self.inorder(node.children[-1], result)
        return result


# 테스트 코드
tree = Tree234()
for v in [10, 20, 5, 6, 12, 30, 7, 17]:
    tree.insert(v)

print("중위 순회:", tree.inorder(tree.root))

print("탐색 12:", tree.search(tree.root, 12))
print("탐색 25:", tree.search(tree.root, 25))

tree.delete(6)
print("6 삭제 후:", tree.inorder(tree.root))

tree.delete(30)
print("30 삭제 후:", tree.inorder(tree.root))
