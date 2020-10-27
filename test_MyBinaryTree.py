import unittest
import MyBinaryTree
import MyBinaryTree.Node

class MyTestCase(unittest.TestCase):

    #test null
    def test_findLCAOfEmptyTree(self):
        tree = MyBinaryTree.Node
        self.assertNull(tree.findLCA(1,2), "LCA of empty tree is null")

    #test tree with one node
    def test_findLCAOfTreeWithOneNode(self):
        root = MyBinaryTree.Node(1)

        result = MyBinaryTree.findLCA(1, 1)
        self.assertEquals(result, 1, "LCA of a tree with one root node with value 1 is 1.")

    #test standard non-empty tree
    def test_findLCAOfStandardNonEmptyTree(self):
        root = MyBinaryTree.Node(1)
        root.left = MyBinaryTree.Node(2)
        root.right = MyBinaryTree.Node(3)
        root.left.left = MyBinaryTree.Node(4)
        root.left.right = MyBinaryTree.Node(5)
        root.right.left = MyBinaryTree.Node(6)
        root.right.right = MyBinaryTree.Node(7)

        result = MyBinaryTree.findLCA(4,7)
        self.assertEquals(result, 1, "LCA of nodes 4 and 7 is root node 1.")


if __name__ == '__main__':
    unittest.main()
