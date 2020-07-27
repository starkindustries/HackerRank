class Node:
    left = None
    right = None
    value = None

    def __init__(self, tempValue = None, tempLeft = None, tempRight = None):
        self.value = tempValue
        self.left = tempLeft
        self.right = tempRight        

    def levelOrderTraversal(self):
        levelMap = self.levelOrderHelper(0, {})
        for key, val in levelMap.items():
            print(f"{key}: {val}")        
    
    def levelOrderHelper(self, level, levelMap):        
        self.addToLevelMap(self.value, level, levelMap)
        if self is None:
            return
        # handle left node
        if self.left:
            self.left.levelOrderHelper(level + 1, levelMap)
        else:
            self.addToLevelMap(None, level + 1, levelMap)
        # handle right node
        if self.right:
            self.right.levelOrderHelper(level + 1, levelMap)
        else:
            self.addToLevelMap(None, level + 1, levelMap)
        return levelMap

    def addToLevelMap(self, value, level, levelMap):
        if level in levelMap:
            levelMap[level].append(value)
        else:
            levelMap[level] = [value]

def sumRootToLeaf(tree):
    total = sumRootToLeafHelper(tree, 0)
    print(f"Total: {total}")

def sumRootToLeafHelper(node, current):
    if node is None:
        return 0
    # if node is leaf node, return number
    current = current * 10 + node.value
    if node.left is None and node.right is None:
        return current
    # if not leaf node, return sum of branches
    return sumRootToLeafHelper(node.left, current) + sumRootToLeafHelper(node.right, current)
    #     1 
    #  2     3
    # 
    # current = 1
    # left: current = 12  

if __name__ == "__main__":
    node = Node(1)
    node.left = Node(2)
    node.right = Node(3)
    node.left.left = Node(4)
    # node.left.right = Node(5)
    # node.left.right.left = Node(7)
    # node.left.right.right = Node(8)    
    # node.right.right = Node(6)
    # node.right.right.left = Node(9)    
    node.levelOrderTraversal()
    sumRootToLeaf(node)
    print("==================================")
    sumRootToLeaf(None)
    print("==================================")
    sumRootToLeaf(Node(9))
    print("==================================")
    node = Node(1)
    node.left = Node(2)
    node.right = Node(3)
    sumRootToLeaf(node)

