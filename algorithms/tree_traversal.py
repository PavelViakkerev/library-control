def inorder(node, result=None):
    if result is None:
        result = []
    if node is not None:
        inorder(node.left, result)
        result.append(node.book)
        inorder(node.right, result)
    return result


def preorder(node, result=None):
    if result is None:
        result = []
    if node is not None:
        result.append(node.book)
        preorder(node.left, result)
        preorder(node.right, result)
    return result


def postorder(node, result=None):
    if result is None:
        result = []
    if node is not None:
        postorder(node.left, result)
        postorder(node.right, result)
        result.append(node.book)
    return result
