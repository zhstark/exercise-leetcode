## [173 Binary Search Tree Iterator](https://leetcode.com/problems/binary-search-tree-iterator/)  :triangular_flag_on_post:

> Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

> Calling next() will return the next smallest number in the BST.

> - next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
> - You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.

In order to run `next()` in O(1) time and O(h) memory, we can not inorder sort the tree in advance, but inorder traverse it step by step. 

So using a stack to store all the left of one node, like inorder iteratively. 

Java

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
class BSTIterator {
    
    private Stack<TreeNode> stack=new Stack();
    public BSTIterator(TreeNode root) {
        putAllLeft(root);
    }
    
    /** @return the next smallest number */
    public int next() {
        TreeNode node= stack.pop();
        putAllLeft(node.right);
        return node.val;
    }
    
    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        return !stack.isEmpty();
    }
    private void putAllLeft(TreeNode node){
        while(node!=null){
            stack.push(node);
            node=node.left;
        }
    }
}
```

C++

```Cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class BSTIterator {
public:
    BSTIterator(TreeNode* root) {
        putAllLeft(root);
    }
    
    /** @return the next smallest number */
    int next() {
        TreeNode* node=s.top();
        s.pop();
        putAllLeft(node->right);
        return node->val;
    }
    
    /** @return whether we have a next smallest number */
    bool hasNext() {
        return !s.empty();
    }
private:
    stack<TreeNode*> s;
    void putAllLeft(TreeNode* root){
        while(root!=NULL){
            s.push(root);
            root=root->left;
        }
    }
};
```
## 105. Construct Binary Tree from Preorder and Inorder Traversal

In a binary tree, the first elements in the preorder is the value of the root. In inorder, the left elements of the root value are all values of the left subtree, the right elements of the root value are all values of the right subtree. 

In the begining, we get the root value by the 1st element in preorder, and we find this value in inorder to split the inorder into left subtree's inorder and right subtree's inorder. By counting the number of elements we can also split the preorder into left subtree's preorder and right subtree's preorder. Then we get the root of subtree and split it again. The time complexity is O(n^2), the spacial complexity is O(n).

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        // firstly check if the input is valid.
        if(preorder.size()==0 || inorder.size()!=preorder.size())   return NULL;
        int n=preorder.size();
        // build the tree recursivly.
        TreeNode* root=helper(preorder,0,n,inorder, 0, n);
        return root;
    }
private:
    TreeNode* helper(vector<int>& pre, int l1, int r1, vector<int>& in, int l2, int r2){
        if(l1>=r1)  return NULL;
        int val=pre[l1];
        TreeNode* root=new TreeNode(val);
        int p=l2;
        for(;p<r2;++p){
            if(in[p]==val)  break;
        }
        root->left=helper(pre,l1+1,l1+p-l2+1, in,l2,p);
        root->right=helper(pre,l1+p-l2+1,r1, in, p+1,r2);
        return root;
    }
};
```

## 106. Construct Binary Tree from Inorder and Postorder Traversal

[link](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)

Almost the same as 105

```cpp

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        if(inorder.size()==0 || inorder.size()!=postorder.size())   return NULL;
        
        int n=inorder.size();
        TreeNode *root=helper(inorder, 0,n, postorder,0,n);
        return root;
    }
private:
    TreeNode* helper(vector<int>& in, int l1,int r1, vector<int>& post, int l2, int r2){
        if (l1>=r1) return NULL;
        int val=post[r2-1];
        TreeNode *root=new TreeNode(val);
        int p=l1;
        //l1-p is left subtree
        for(;p<r1; ++p){
            if(in[p]==val)  break;
        }
        root->left=helper(in, l1, p, post, l2, l2+p-l1);
        root->right=helper(in, p+1, r1, post, l2+p-l1, r2-1);
        return root;
    }
};
```
