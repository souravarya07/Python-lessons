class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)

class BST:
    def __init__(self):
        self.root = None

    def _insert(self, start_node, new_node):
        if start_node.value == new_node.value:
            return None
        elif start_node.value > new_node.value:
            if start_node.left is None:
                start_node.left = new_node
            else:
                self._insert(start_node.left, new_node)
        else:
            if start_node.right is None:
                start_node.right = new_node
            else:
                self._insert(start_node.right, new_node)

    def insert(self,val):
        new_node = Node(val)
        if self.root == None:
            self.root = new_node
        else:
            self._insert(self.root, new_node)

    def printBF(self):
        q = []
        if self.root:
            q.append(self.root)
        while len(q) > 0:
            if q[0].left:
                q.append(q[0].left)
            if q[0].right:
                q.append(q[0].right)

            temp = q.pop(0)
            print(temp, end=',')
        print()

    def _printInDF(self, start):
        if start is None:
            return
        self._printInDF(start.left)
        print(start,end=" ")
        self._printInDF(start.right)

    def _printPreDF(self,start):
        if start is None:
            return
        print(start, end=" ")
        self._printPreDF(start.left)
        self._printPreDF(start.right)

    def _printPostDF(self, start):
        if start is None:
            return
        self._printPostDF(start.left)
        self._printPostDF(start.right)
        print(start, end=" ")

    def printDF(self, order="in"):
        if order == "in":
            self._printInDF(self.root)
        elif order == "pre":
            self._printPreDF(self.root)
        else:
            self._printPostDF(self.root)
        print()

    def _search(self, start, target):
        if start.value == target.value:
            return start
        elif start.value > target.value:
            if start.left:
                return self._search (start.left , target)
            return None
        else:
            if start.right:
                return self._search(start.right, target)
            return None

    def search(self, target):
        if self.root:
            return self._search(self.root, target)




