# This is the class of the input root. Do not edit it.


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self


def branchSums(root):
    # Write your code here.
    result = []
    branchSumHelper(root, result, 0)
    return result


def branchSumHelper(root, branchSums, currentSum):
    if root.left is None and root.right is None:
        # found a leaf node
        branchSums.append(currentSum + root.value)
    if root.left is not None:
        branchSumHelper(root.left, branchSums, currentSum + root.value)
    if root.right is not None:
        branchSumHelper(root.right, branchSums, currentSum + root.value)
