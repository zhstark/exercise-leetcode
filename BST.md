## In Order iterative

1、如果当前 node 有左子树，先把该节点放到栈里，然后指向其左子树

2、如果没有了左子树，那么输出该节点，然后指向其右子树，回到第一步

##### No 173

```py
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack=[]
        curr=root
        while curr:
            self.stack.append(curr)
            curr=curr.left

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        node=self.stack.pop()
        curr=node.right
        while curr:
            self.stack.append(curr)
            curr=curr.left
    
        return node.val

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return self.stack!=[]
```

## Pre-Order

###### ------No 617 -------------------------

in Python:
`x or y` = `x if x else y` = `x ? x : y` in C++
t1=TreeNode(0)   
t2=TreeNode(1)
`t1 and t2` = t2
`t1 or t2` = t1
t1=None
t1 and t2=None
t1 or t2=t2   

*另外在递归里先调用本身然后 return 有点不理解*



```py
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
```