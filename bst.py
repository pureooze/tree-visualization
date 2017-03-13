class BST:
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.value = value

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getVal(self):
        return self.value

    def insertNode(self, value):
        if self.value == None:
            self.value = value
        else:
            if self.value > value:
                if self.left is None:
                    self.left = BST(value)
                else:
                    self.left.insertNode(value)
            elif self.right is None:
                self.right = BST(value)
            else:
                self.right.insertNode(value)

    def search(self, key):
        if self.value == key:
            return [self.value]
        elif key < self.value:
            return [self.value, self.left.search(key)]
        else:
            return [self.value, self.right.search(key)]

    def getDepth(self):
        if self.value is None:
            return
        else:
            if self.left is not None:
                self.left_depth = self.left.getDepth()
            else:
                self.left_depth = 0

            if self.right is not None:
                self.right_depth = self.right.getDepth()
            else:
                self.right_depth = 0

            return max(self.left_depth, self.right_depth)+1

    def inorderTraversal(self):
        if self.value is None:
            return
        else:
            self.nodes = []
            if self.left is not None:
                self.nodes.append(self.left.inorderTraversal())
            else:
                self.nodes.append(None)
                
            self.nodes.append(self.value)

            if self.right is not None:
                self.nodes.append(self.right.inorderTraversal())
            else:
                self.nodes.append(None)
                
            return self.nodes


if __name__ == "__main__":
    a = BST(10)
    a.insertNode(2)
    a.insertNode(3)
    a.insertNode(40)

    print(a.right.value)
    print(a.left.value)

