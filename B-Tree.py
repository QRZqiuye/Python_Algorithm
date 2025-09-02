class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t                  # 최소 차수
        self.keys = []              # 키 리스트
        self.children = []          # 자식 노드 리스트
        self.leaf = leaf            # 리프 여부


class BTree:
    def __init__(self, t):
        self.root = BTreeNode(t, leaf=True)
        self.t = t

    # 탐색 알고리즘
    def search(self, node, key):
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        if i < len(node.keys) and key == node.keys[i]:
            return node, i
        if node.leaf:
            return None
        return self.search(node.children[i], key)

    # 삽입 알고리즘
    def insert(self, key):
        root = self.root
        if len(root.keys) == (2 * self.t - 1):
            new_root = BTreeNode(self.t, leaf=False)
            new_root.children.append(root)
            self.split_child(new_root, 0)
            self.root = new_root
            self.insert_non_full(new_root, key)
        else:
            self.insert_non_full(root, key)

    def insert_non_full(self, node, key):
        i = len(node.keys) - 1
        if node.leaf:
            node.keys.append(key)
            node.keys.sort()
        else:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == (2 * self.t - 1):
                self.split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self.insert_non_full(node.children[i], key)

    def split_child(self, parent, i):
        t = self.t
        node = parent.children[i]
        new_node = BTreeNode(t, leaf=node.leaf)

        parent.keys.insert(i, node.keys[t - 1])
        parent.children.insert(i + 1, new_node)

        new_node.keys = node.keys[t:(2 * t - 1)]
        node.keys = node.keys[0:(t - 1)]

        if not node.leaf:
            new_node.children = node.children[t:(2 * t)]
            node.children = node.children[0:t]

    # 삭제 알고리즘
    def delete(self, node, key):
        t = self.t
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1

        if i < len(node.keys) and key == node.keys[i]:
            if node.leaf:  # 리프에서 삭제
                node.keys.pop(i)
            else:  # 내부 노드에서 삭제
                if len(node.children[i].keys) >= t:
                    pred = self.get_predecessor(node.children[i])
                    node.keys[i] = pred
                    self.delete(node.children[i], pred)
                elif len(node.children[i + 1].keys) >= t:
                    succ = self.get_successor(node.children[i + 1])
                    node.keys[i] = succ
                    self.delete(node.children[i + 1], succ)
                else:
                    self.merge(node, i)
                    self.delete(node.children[i], key)
        elif not node.leaf:
            if len(node.children[i].keys) < t:
                self.fill(node, i)
            if i > len(node.keys):
                self.delete(node.children[i - 1], key)
            else:
                self.delete(node.children[i], key)

    def get_predecessor(self, node):
        while not node.leaf:
            node = node.children[-1]
        return node.keys[-1]

    def get_successor(self, node):
        while not node.leaf:
            node = node.children[0]
        return node.keys[0]

    def merge(self, parent, i):
        child = parent.children[i]
        sibling = parent.children[i + 1]

        child.keys.append(parent.keys.pop(i))
        child.keys.extend(sibling.keys)
        if not child.leaf:
            child.children.extend(sibling.children)

        parent.children.pop(i + 1)

    def fill(self, parent, i):
        t = self.t
        if i > 0 and len(parent.children[i - 1].keys) >= t:
            self.borrow_from_prev(parent, i)
        elif i < len(parent.children) - 1 and len(parent.children[i + 1].keys) >= t:
            self.borrow_from_next(parent, i)
        else:
            if i < len(parent.children) - 1:
                self.merge(parent, i)
            else:
                self.merge(parent, i - 1)

    def borrow_from_prev(self, parent, i):
        child = parent.children[i]
        sibling = parent.children[i - 1]

        child.keys.insert(0, parent.keys[i - 1])
        parent.keys[i - 1] = sibling.keys.pop()
        if not sibling.leaf:
            child.children.insert(0, sibling.children.pop())

    def borrow_from_next(self, parent, i):
        child = parent.children[i]
        sibling = parent.children[i + 1]

        child.keys.append(parent.keys[i])
        parent.keys[i] = sibling.keys.pop(0)
        if not sibling.leaf:
            child.children.append(sibling.children.pop(0))

    # 중위 순회
    def inorder(self, node, result=None):
        if result is None:
            result = []
        if node.leaf:
            result.extend(node.keys)
        else:
            for i in range(len(node.keys)):
                self.inorder(node.children[i], result)
                result.append(node.keys[i])
            self.inorder(node.children[-1], result)
        return result


# 최소 차수 t=2 인 B-트리
btree = BTree(2)

# 삽입
for v in [10, 20, 5, 6, 12, 30, 7, 17]:
    btree.insert(v)

print("중위 순회 (삽입 후):", btree.inorder(btree.root))

# 탐색
print("탐색 12:", btree.search(btree.root, 12) is not None)
print("탐색 25:", btree.search(btree.root, 25) is not None)

# 삭제
btree.delete(btree.root, 6)
print("6 삭제 후:", btree.inorder(btree.root))

btree.delete(btree.root, 13)  # 존재하지 않음
print("13 삭제 시도 후:", btree.inorder(btree.root))

btree.delete(btree.root, 7)
print("7 삭제 후:", btree.inorder(btree.root))

btree.delete(btree.root, 4)  # 존재하지 않음
print("4 삭제 시도 후:", btree.inorder(btree.root))

btree.delete(btree.root, 12)
print("12 삭제 후:", btree.inorder(btree.root))
