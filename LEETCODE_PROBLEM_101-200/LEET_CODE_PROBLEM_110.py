"""
Description:

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

-> 즉, 양 sub-trees 의 깊이 차이가 1 이하인 binary tree 를 의미한다.
-> 문제에서 입력은 전위순회 형태로 주어진다.
Example 0)
Input: root = [3,9,20,null,null,15,7]
Output: true

Tree 형태
         3
      9    20
         15   7

Example 1)
Input: root = [1,2,2,3,3,null,null,4,4]
Output: Output: false

Tree 형태
        1
     2    2
  3    3
4   4

Example 2)
Input: root = []
Output: true
"""

class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''Someone's good solution'''
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return bool(self.check(root))


    def check(self, node):
        if not node:
            return True
        l, r = self.check(node.left), self.check(node.right)
        return max(l, r) + 1 if l and r and abs(l - r) < 2 else False

'''Example.1 : 3,9,20,null,null,15,7'''
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.left.left = None
root.left.right = None
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
"""
Example.2 : 1,2,2,3,3,null,null,4,4
           1
       2       2
    3     3  N    N
4     4
"""

root_1 = TreeNode(val=1)
root_1.left = TreeNode(val=2)
root_1.right = TreeNode(val=2)
root_1.left.left = TreeNode(val=3)
root_1.left.right = TreeNode(val=3)
root_1.right.left = None
root_1.right.right = None
root_1.left.left.left = TreeNode(val=4)
root_1.left.left.right = TreeNode(val=4)

'''Solution Check'''
"""
Example.3) [1,null,2,null,3]
       1
  null    2

        null  3
"""

root_2 = TreeNode(val=1)
root_2.left = None
root_2.right = TreeNode(val=2)
root_2.right.right = TreeNode(val=3)

"""
Example.4) [1,2,2,3,null,null,3,4,null,null,4]
TreeNode{val: 1, left: TreeNode{val: 2, left: TreeNode{val: 3, left: TreeNode{val: 4, left: None, right: None}, right: None}, right: None}, 
    right: TreeNode{val: 2, left: None, right: TreeNode{val: 3, left: None, right: TreeNode{val: 4, left: None, right: None}}}}
                        1
                   2         2
                3     N     N   3      
            4     N            N   4
"""
root_3 = TreeNode(val=1)
root_3.left = TreeNode(val=2)
root_3.right = TreeNode(val=2)
root_3.left.left = TreeNode(val=3)
root_3.right.right = TreeNode(val=3)
root_3.left.left.left = TreeNode(val=4)
root_3.right.right.right = TreeNode(val=4)

solver = Solution()
print(solver.isBalanced(root_1))
# print(solver.isBalanced(root))
# print(solver.isBalanced(root_3))
# print(solver.isBalanced(root_2))
# print(solver.isBalanced(TreeNode(None)))

