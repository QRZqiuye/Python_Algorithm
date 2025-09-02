RED = True
BLACK = False

class Node:
    def __init__(self, key, color=RED, left=None, right=None, parent=None):
        self.key = key
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent


class RedBlackTree:
    def __init__(self):
        self.NIL = Node(key=None, color=BLACK)  # NIL 리프 노드
        self.root = self.NIL

    # 탐색 알고리즘 (BST와 동일)
    def search(self, node, key):
        if node == self.NIL or key == node.key:
            return node
        if key < node.key:
            return self.search(node.left, key)
        else:
            return self.search(node.right, key)

    # 왼쪽 회전
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    # 오른쪽 회전
    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y
        x.parent = y.parent
        if y.parent == None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    # 삽입 알고리즘
    def insert(self, key):
        node = Node(key)
        node.left = self.NIL
        node.right = self.NIL

        parent = None
        current = self.root
        while current != self.NIL:
            parent = current
            if node.key < current.key:
                current = current.left
            else:
                current = current.right

        node.parent = parent
        if parent == None:
            self.root = node
        elif node.key < parent.key:
            parent.left = node
        else:
            parent.right = node

        node.color = RED
        self.fix_insert(node)

    def fix_insert(self, k):
        while k.parent and k.parent.color == RED:
            if k.parent == k.parent.parent.left:
                u = k.parent.parent.right
                if u.color == RED:  # Case 1
                    k.parent.color = BLACK
                    u.color = BLACK
                    k.parent.parent.color = RED
                    k = k.parent.parent
                else:
                    if k == k.parent.right:  # Case 2
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = BLACK  # Case 3
                    k.parent.parent.color = RED
                    self.right_rotate(k.parent.parent)
            else:
                u = k.parent.parent.left
                if u.color == RED:
                    k.parent.color = BLACK
                    u.color = BLACK
                    k.parent.parent.color = RED
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    self.left_rotate(k.parent.parent)
        self.root.color = BLACK

    # 삭제 알고리즘
    def delete(self, key):
        z = self.search(self.root, key)
        if z == self.NIL:
            print("삭제할 노드가 없습니다:", key)
            return

        y = z
        y_original_color = y.color
        if z.left == self.NIL:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        if y_original_color == BLACK:
            self.fix_delete(x)

    def transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def fix_delete(self, x):
        while x != self.root and x.color == BLACK:
            if x == x.parent.left:
                s = x.parent.right
                if s.color == RED:  # Case 1
                    s.color = BLACK
                    x.parent.color = RED
                    self.left_rotate(x.parent)
                    s = x.parent.right
                if s.left.color == BLACK and s.right.color == BLACK:  # Case 2
                    s.color = RED
                    x = x.parent
                else:
                    if s.right.color == BLACK:  # Case 3
                        s.left.color = BLACK
                        s.color = RED
                        self.right_rotate(s)
                        s = x.parent.right
                    s.color = x.parent.color  # Case 4
                    x.parent.color = BLACK
                    s.right.color = BLACK
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == RED:
                    s.color = BLACK
                    x.parent.color = RED
                    self.right_rotate(x.parent)
                    s = x.parent.left
                if s.left.color == BLACK and s.right.color == BLACK:
                    s.color = RED
                    x = x.parent
                else:
                    if s.left.color == BLACK:
                        s.right.color = BLACK
                        s.color = RED
                        self.left_rotate(s)
                        s = x.parent.left
                    s.color = x.parent.color
                    x.parent.color = BLACK
                    s.left.color = BLACK
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = BLACK

    # 최소값 노드 찾기
    def minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node

    # 중위 순회 (오름차순)
    def inorder(self, node, result=None):
        if result is None:
            result = []
        if node != self.NIL:
            self.inorder(node.left, result)
            result.append((node.key, "R" if node.color == RED else "B"))
            self.inorder(node.right, result)
        return result


# 테스트 코드
rbt = RedBlackTree()
for v in [20, 15, 25, 10, 5, 1, 30, 35, 40]:
    rbt.insert(v)

print("중위 순회 (삽입 후):", rbt.inorder(rbt.root))

print("탐색 15:", rbt.search(rbt.root, 15).key if rbt.search(rbt.root, 15) else "없음")
print("탐색 100:", "찾음" if rbt.search(rbt.root, 100) else "없음")

rbt.delete(25)
print("25 삭제 후:", rbt.inorder(rbt.root))

rbt.delete(20)
print("20 삭제 후:", rbt.inorder(rbt.root))
