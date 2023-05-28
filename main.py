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
        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    return
                else:
                    current = current.left
            if value > current.value:
                if current.right is None:
                    current.right = new_node
                    return
                else:
                    current = current.right

    def search_recursive(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def search_iterative(self, value):
        current = self.root
        while current is not None and current.value != value:
            if value < current.value:
                current = current.left
            else:
                current = current.right
        return current

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
        current = node
        while current.left is not None:
            current = current.left
        return current

    def get_min(self):
        if self.root is None:
            return None
        return self._get_min(self.root)

    def _get_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.value

    def get_max(self):
        if self.root is None:
            return None
        return self._get_max(self.root)

    def _get_max(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current.value

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
        current = self.root
        while current is not None or stack:
            while current is not None:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.value)
            current = current.right
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

    def postorder_recursive(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node, result):
        if node is not None:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)

    def preorder_iterative(self):
        result = []
        stack = [self.root]
        while stack:
            node = stack.pop()
            if node:
                result.append(node.value)
                stack.append(node.right)
                stack.append(node.left)
        return result

    def postorder_iterative(self):
        result = []
        stack = []
        current = self.root
        while True:
            while current:
                if current.right:
                    stack.append(current.right)
                stack.append(current)
                current = current.left
            current = stack.pop()
            if current.right and stack and stack[-1] == current.right:
                stack.pop()
                stack.append(current)
                current = current.right
            else:
                result.append(current.value)
                current = None
            if not stack:
                break
        return result



bst = BST()
bst.insert_recursive(2)
bst.insert_recursive(3)
bst.insert_recursive(15)
bst.insert_recursive(11)
bst.insert_recursive(7)
bst.insert_recursive(14)

print(bst.exists(6))
print(bst.exists(9))

print(bst.get_min())
print(bst.get_max())

bst.delete(6)
print(bst.inorder_recursive())
print(bst.inorder_iterative())
print(bst.preorder_recursive())
print(bst.preorder_iterative())
print(bst.postorder_recursive())
print(bst.postorder_iterative())