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

    def postorder_iterative(self):
        result = []
        stack = []
        cur = self.root
        while True:
            while cur:
                if cur.right:
                    stack.append(cur.right)
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if cur.right and stack and stack[-1] == cur.right:
                stack.pop()
                stack.append(cur)
                cur = cur.right
            else:
                result.append(cur.value)
                cur = None
            if not stack:
                break
        return result
    
    def savetofile(self, filename):
        with open(filename, 'w') as file:
            self._savetofile(self.root, file)
    def _savetofile(self, node, file):
        if node is None:
            return
        file.write(str(node.value)+'\n')
        self._savetofile(node.left, file)
        self._savetofile(node.right, file)

bst = BST()
bst.insert_recursive(2)
bst.insert_recursive(3)
bst.insert_recursive(15)
bst.insert_recursive(11)
bst.insert_recursive(7)
bst.insert_recursive(14)

print(bst.exists(11))
print(bst.exists(9))

print(bst.get_min())
print(bst.get_max())
bst.delete(6)
print(bst.inorder_recursive())
print(bst.preorder_recursive())
print(bst.postorder_recursive())
print(bst.postorder_iterative())
print(bst.preorder_iterative())
print(bst.inorder_iterative())
bst.savetofile('main.txt')