

class BinaryTree:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def preOrder(node: BinaryTree, res: list):
    if node is None:
        return res
    res.append(node.value)
    print(res)
    preOrder(node.left, res)
    preOrder(node.right, res)





