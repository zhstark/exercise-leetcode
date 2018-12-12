# No.543
# DFS with Linked List Graph


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        self.maxDis = 0

        def dfs(root):
            if not root:
                return 0
            L = dfs(root.left)
            R = dfs(root.right)
            self.maxDis = max(self.maxDis, L+R+1)
            return max(L, R)+1

        dfs(root)
        return self.maxDis-1
