## In Order iterative
中序遍历即将各节点从小到大输出。

1、如果当前 node 有左子树，先把该节点放到栈里，然后指向其左子树

2、如果没有了左子树，那么输出该节点，然后指向其右子树，回到第一步

### 递归写法

```Java
public void inOrder(TreeNode root){
    if(root==null)
        return;
    Stack<TreeNode> stack=new Stack();
    TreeNode curr=root;
    while(curr!=null || !stack.isEmpty()){
        if(curr!=null){
            stack.push(curr);
            curr=curr.left;
        }
        else{
            curr=stack.pop();
            System.out.println(curr.val;
            curr=curr.right;
        }
    }
}
```

### No 173

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

### [426 Convert Binary Search Tree to Sorted Doubly Linked List](https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/)   :triangular_flag_on_post: 

C++ 
```cpp
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;

    Node() {}

    Node(int _val, Node* _left, Node* _right) {
        val = _val;
        left = _left;
        right = _right;
    }
};
*/
class Solution {
public:
    Node* treeToDoublyList(Node* root) {
        if(!root)   return NULL;
        inorder(root);
        last->right=first;
        first->left=last;
        return first;
        
    }
private:
    Node* first=NULL;
    Node* last=NULL;
    
    void inorder(Node* node){
        if(node!=NULL){        
            inorder(node->left);
            if(last!=NULL){
                last->right=node;
                node->left=last;    
            }
            else
                first=node;
            
            last=node;
            inorder(node->right);
        }
        return;
    }
};
```

Java
```Java
/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;

    public Node() {}

    public Node(int _val,Node _left,Node _right) {
        val = _val;
        left = _left;
        right = _right;
    }
};
*/
class Solution {
    private Node first=null;
    private Node last=null;
    
    private void inOrder(Node node){
        if(node!=null){
            inOrder(node.left);
            if(last!=null){
                last.right=node;
                node.left=last;
            }
            else
                first=node;
            
            last=node;
            inOrder(node.right);
        }
        return;
        
    }
    public Node treeToDoublyList(Node root) {
        first=null;
        last=null;
        if(root ==null)   return null;
        inOrder(root);
        first.left=last;
        last.right=first;
        return first;
    }
}
```

## Pre-Order

### Iteration

```Java
public void preOrder(TreeNode root){
    if(root==null)  return;
    Stack<TreeNode> stack=new Stack();
    stack.push(root);
    while(!stack.isEmpty()){
        TreeNode node=stack.pop();
        System.out.println(node.val);
        if(node.left!=null)
            stack.push(node.left);
        if(node.right!=null)
            stack.push(node.right);
    }
}
```
### No 617

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

## [95 Unique Binary Search Trees II](https://leetcode.com/problems/unique-binary-search-trees-ii/)

> Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Practice Recursive

```Java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public List<TreeNode> generateTrees(int n) {
        List<TreeNode> ans=new ArrayList();
        if(n<1) return ans;
        return generateSubTree(1, n);
    }  
    public List<TreeNode> generateSubTree(int start, int end){
        List<TreeNode> ans=new ArrayList();
        if(start>end){
            ans.add(null);
            return ans;
        }     
        for(int i=start; i<=end; ++i){
            List<TreeNode> leftTree=generateSubTree(start, i-1);
            List<TreeNode> rightTree=generateSubTree(i+1, end);
            for(TreeNode left: leftTree){
                for(TreeNode right:rightTree){
                    TreeNode root=new TreeNode(i);
                    root.left=left;
                    root.right=right;
                    ans.add(root);
                }
            }
        }
        return ans;
    }
}
```

## Post-Order

### 迭代法

```Java
/**
 * 后续遍历栈方式
 * 需要增加一个节点记录，用于记录上次出栈的节点
 * 1、如果栈顶元素非空且左节点存在，将其入栈，重复该过程。若不存在则进入第2步（该过程和中序遍历一致）
 * 2、判断上一次出栈节点是否当前节点的右节点，或者当前节点是否存在右节点，满足任一条件，将当前节点输出，并出栈。否则将右节点压栈。跳至第1步
 */
static void postTraversalStack(Node root) {
    Stack<Node> stack = new Stack<>();
    stack.push(root);
    Node lastNode = null;
    while (!stack.isEmpty()) {
        while (stack.peek().left != null) {
            stack.push(stack.peek().left);
        }
        while (!stack.isEmpty()) {
            if (lastNode == stack.peek().right || stack.peek().right == null) {
                Node node = stack.pop();
                System.out.print(node.val + " ");
                lastNode = node;
            } else if (stack.peek().right != null) {
                stack.push(stack.peek().right);
                break;
            }
        }
    }
}
```