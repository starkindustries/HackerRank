# ============================================
# Testing Code
import unittest
from BranchSums import BinaryTree
from BranchSums import branchSums


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        tree = BinaryTree(1)
        self.assertEqual(branchSums(tree), [1])

    def test_case_2(self):
        tree = BinaryTree(1).insert([2])
        self.assertEqual(branchSums(tree), [3])

    def test_case_3(self):
        tree = BinaryTree(1).insert([2, 3])
        self.assertEqual(branchSums(tree), [3, 4])

    def test_case_4(self):
        tree = BinaryTree(1).insert([2, 3, 4, 5])
        self.assertEqual(branchSums(tree), [7, 8, 4])

    def test_case_5(self):
        tree = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(branchSums(tree), [15, 16, 18, 10, 11])

    def test_case_6(self):
        tree = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1, 1])
        self.assertEqual(branchSums(tree), [15, 16, 18, 9, 11, 11, 11])

    def test_case_7(self):
        tree = BinaryTree(0)
        tree.left = BinaryTree(1)
        tree.left.left = BinaryTree(10)
        tree.left.left.left = BinaryTree(100)
        self.assertEqual(branchSums(tree), [111])

    def test_case_8(self):
        tree = BinaryTree(0)
        tree.right = BinaryTree(1)
        tree.right.right = BinaryTree(10)
        tree.right.right.right = BinaryTree(100)
        self.assertEqual(branchSums(tree), [111])

    def test_case_9(self):
        tree = BinaryTree(0)
        tree.left = BinaryTree(9)
        tree.right = BinaryTree(1)
        tree.right.left = BinaryTree(15)
        tree.right.right = BinaryTree(10)
        tree.right.right.left = BinaryTree(100)
        tree.right.right.right = BinaryTree(200)
        self.assertEqual(branchSums(tree), [9, 16, 111, 211])


if __name__ == "__main__":
    unittest.main()
