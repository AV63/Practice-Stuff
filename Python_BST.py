
class Node:
    def __init__(self,data):
        self.left =None
        self.right =None
        self.data = data


class BinaryTree:
    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data < root.data:
                current = self.insert(root.left, data)
                root.left = current
            else:
                current = self.insert(root.right, data)
                root.right = current
        return root

    def getHeight(self, root):
        if not root:
            return -1
        elif not root.left and not root.right:
            return 0
        else:
            left_height = self.getHeight(root.left)
            right_height = self.getHeight(root.right)
        return max(left_height, right_height) + 1


n = int(input('Enter number of elements to insert '))
myTree = BinaryTree()
root = None
for i in range(n):
    data = int(input('Enter the data you want to insert'))
    root = myTree.insert(root, data)
height = myTree.getheight(root)
print('The height of the tree is ', height)
