

class BinaryTree:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

node1 = BinaryTree(1)
node2 = BinaryTree(2)
node3 = BinaryTree(3)
node4 = BinaryTree(4)
node5 = BinaryTree(5)
node6 = BinaryTree(6)
node7 = BinaryTree(7)
node8 = BinaryTree(8)
node9 = BinaryTree(9)
node10 = BinaryTree(10)
node11 = BinaryTree(11)



node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
node4.left = node8
node4.right = node9
node5.left = node10
node5.right = node11


def preOrder(node: BinaryTree):
    if node is None:
        return
    print(node.value)
    preOrder(node.left)
    preOrder(node.right)

if __name__ == "__main__":
    preOrder(node1)




