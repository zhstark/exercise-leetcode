## [314 Binary Tree Vertical Order Traversal](https://leetcode.com/problems/binary-tree-vertical-order-traversal/)  :triangular_flag_on_post:

> Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

> If two nodes are in the same row and column, the order should be from left to right.

BFS uses queue

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
    public List<List<Integer>> verticalOrder(TreeNode root) {
        List<List<Integer>> ans=new ArrayList();
        if(root==null)  return ans;
        Map<Integer, List<Integer>> map=new TreeMap();
        Queue<TreeNode> treeQ=new LinkedList();
        Queue<Integer> indexQ=new LinkedList();
        treeQ.add(root);
        indexQ.add(0);
        while(!treeQ.isEmpty()){
            TreeNode node=treeQ.poll();
            int x=indexQ.poll();
            if(!map.containsKey(x)){
                map.put(x, new ArrayList<Integer>());
            }
            map.get(x).add(node.val);
            // if(map.containsKey(x)){
            //     List<Integer> temp=map.get(x);
            //     temp.add(node.val);
            // }
            // else{
            //     List<Integer> list=new ArrayList();
            //     list.add(node.val);
            //     map.put(x, list);
            // }
            if(node.left!=null){
                treeQ.add(node.left);
                indexQ.add(x-1);
            }
            if(node.right!=null){
                treeQ.add(node.right);
                indexQ.add(x+1);
            }
        }
        for(List<Integer> v: map.values()){
            ans.add(v);
        }
        return ans;
    }
}
```

## [199 Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) :triangular_flag_on_post:

> Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

BFS, get the elements layer by layer

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
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> ans=new ArrayList();
        if(root==null)  return ans;
        Queue<TreeNode> q=new LinkedList();
        q.add(root);
        while(!q.isEmpty()){
            int len=q.size();
            for(int i=0; i<len; ++i){
                TreeNode node=q.poll();
                if(i==len-1)
                    ans.add(node.val);
                
                if(node.left!=null)
                    q.add(node.left);
                if(node.right!=null)
                    q.add(node.right);
            }
        }
        return ans;
    }
}
```

## 279

BFS不止用在图中

```py
import math
class Solution:
    def numSquares(self, n: int) -> int:
        if n<=0:
            return 0
        
        squares=[i*i for i in range(1, int(math.sqrt(n))+1  )   ]
        toCheck={n}
        cnt=0
        while True:
            temp=set()
            cnt+=1
            for j in toCheck:
                for i in squares:
                    if j<i:
                        break
                    if i==j:
                        return cnt

                    temp.add(j-i)
            toCheck=temp
            

```