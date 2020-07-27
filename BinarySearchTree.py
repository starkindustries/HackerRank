# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import unittest

# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        current = self
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = BST(value)
                    break                
                current = current.left
            else: # elif value >= current.value:
                if current.right is None:
                    current.right = BST(value)
                    break
                current = current.right            
        return self

    def contains(self, value):
        # Write your code here.
        current = self
        while current is not None:
            if current.value == value:
                return True
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
        return False

    def remove(self, value, parent = None):
        current = self
        while current is not None:            
            if value < current.value:
                parent = current
                current = current.left
                continue
            if current.value < value:
                parent = current
                current = current.right
                continue
            # current.value == value: remove current node
            if current.left == current.right == parent == None:
                break # single node BST; do nothing            
            if current.right is None:
                if parent is not None:
                    parent.left = current.left
            else: # get right branch's left most node            
                previous = current
                leftmost = current.right
                while leftmost.left is not None:
                    previous = leftmost
                    leftmost = leftmost.left
                # leftmost is now set to right branch's left most node
                previous.left = leftmost.right
                current.value = leftmost.value
                self.remove(current, parent)
            break
        return self

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BST(10)
        self.assertTrue(root.value == 10)
        root.insert(5)
        self.assertTrue(root.left.value == 5)
        root.insert(15)
        self.assertTrue(root.right.value == 15)
        root.remove(5)
        self.assertTrue(root.left == None)
        root.remove(15)
        self.assertTrue(root.right == None)
        root.remove(10)
        self.assertTrue(root.value == 10)

if __name__ == '__main__':
    unittest.main()