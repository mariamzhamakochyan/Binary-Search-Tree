class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert_recursive(self, value):
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        return node

    def insert_iterative(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return
        cur = self.root
        while True:
            if value < cur.value:
                if cur.left is None:
                    cur.left = new_node
                    return
                else:
                    cur = cur.left
            if value > cur.value:
                if cur.right is None:
                    cur.right = new_node
                    return
                else:
                    cur = cur.right

    def search_recursive(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def search_iterative(self, value):
        cur = self.root
        while cur is not None and cur.value != value:
            if value < cur.value:
                cur = cur.left
            else:
                cur = cur.right
        return cur

    def exists(self, value):
        return self._exists(self.root, value)

    def _exists(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        if value < node.value:
            return self._exists(node.left, value)
        return self._exists(node.right, value)

    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        if node is None:
            return node
        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                temp = self._find_min(node.right)
                node.value = temp.value
                node.right = self._delete(node.right, temp.value)
        return node

    def _find_min(self, node):
        cur = node
        while cur.left is not None:
            cur = cur.left
        return cur

    def get_min(self):
        if self.root is None:
            return None
        return self._get_min(self.root)

    def _get_min(self, node):
        cur = node
        while cur.left is not None:
            cur = cur.left
        return cur.value

    def get_max(self):
        if self.root is None:
            return None
        return self._get_max(self.root)

    def _get_max(self, node):
        cur = node
        while cur.right is not None:
            cur = cur.right
        return cur.value

    def inorder_recursive(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

    def inorder_iterative(self):
        result = []
        stack = []
        cur = self.root
        while cur is not None or stack:
            while cur is not None:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            result.append(cur.value)
            cur = cur.right
        return result

    def preorder_recursive(self):
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node, result):
        if node is not None:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)
