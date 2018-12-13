
# -------------------------No 617 -------------------------
# in Python:
# `x or y` = `x if x else y` =
# `x ? x : y` in C++
# t1=TreeNode(0)   
# t2=TreeNode(1)
# `t1 and t2` = t2
# `t1 or t2` = t1
# t1=None
# t1 and t2=None
# t1 or t2=t2   
#----
# 另外在递归里先调用本身然后 return 有点不理解
# -------------------------
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """

        if t1 and t2:
            node = TreeNode(t1.val+t2.val)
            node.left = self.mergeTrees(t1.left, t2.left)
            node.right = self.mergeTrees(t1.right, t2.right)
            return node

        else:
            return t1 or t2
#         elif t1 and not t2:
#             return t1
#         elif t2 and not t1:
#             return t2
#         else:
#             return None
