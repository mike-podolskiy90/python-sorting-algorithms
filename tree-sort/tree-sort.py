from common.common import arr_to_sort

print(arr_to_sort)


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def insert_node(root, node):
    if root is None:
        root = node
    else:
        if node.value <= root.value:
            if root.left is None:
                root.left = node
            else:
                insert_node(root.left, node)
        else:
            if root.right is None:
                root.right = node
            else:
                insert_node(root.right, node)

    return root


def tree_to_array(node):
    if node is None:
        return []
    return tree_to_array(node.left) + [node.value] + tree_to_array(node.right)


def tree_sort(arr):
    root = None
    for i in range(len(arr)):
        root = insert_node(root, Node(arr[i]))

    return tree_to_array(root)


arr_to_sort = tree_sort(arr_to_sort)

print(arr_to_sort)
