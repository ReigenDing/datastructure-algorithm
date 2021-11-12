

class BinaryTree:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def pre_order(node: BinaryTree, res: list):
    """
    递归实现前序遍历 => DLR
    """
    if node is None:
        return res
    res.append(node.value)
    print(res)
    pre_order(node.left, res)
    pre_order(node.right, res)


def pre_order_traverse(node: BinaryTree):
    """
    非递归实现二叉树前序遍历 => DLR

    """
    stack =  [node]
    res =[]
    while len(stack) > 0:
        _node = stack.pop()
        res.append(_node.value)
        if _node.right is not None:
            stack.append(_node.right)
        if _node.left is not None:
            stack.append(_node.left)
    return res


def post_order_traverse1(node: BinaryTree, res: list):
    """
    递归实现后序遍历 => RLD
    """
    if node is None:
        return
    post_order_traverse1(node.left, res)
    post_order_traverse1(node.right, res)
    res.append(node.value)


def post_order_traverse2(node: BinaryTree):
    """
    非递归实现后续遍历 => RLD
    """
    stack = [node]
    res = []
    while len(stack) > 0:
        _node = stack.pop()
        res.insert(0, _node.value)
        if _node.left is not None:
            stack.append(_node.left)
        if _node.right is not None:
            stack.append(_node.right)
    return res


def in_order_traverse1(node: BinaryTree, res: list):
    """
    递归实现中序遍历 => LDR
    """
    if node is None:
        return 
    in_order_traverse1(node.left, res)
    res.append(node.value)
    in_order_traverse1(node.right, res)


def in_order_traverse2(node: BinaryTree):
    """
    非递归实现中序遍历 = >LDR
    """
    stack = [node]
    temp = []
    pos = node

    while pos or len(stack) > 0:
        if pos:
            stack.append(pos)
            pos = pos.left
        else:
            pos = stack.pop()
            print(pos.value)
            temp.append(pos.value)
            pos = pos.right
    print(temp)
    return temp






