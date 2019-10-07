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

## [1210 Minimum Moves to Reach Target with Rotations](https://leetcode.com/problems/minimum-moves-to-reach-target-with-rotations/)

We need to consider 2 pixel as a unity. So using a `List<> ` to represent a stats, the big picture is still BFS or DFS

```Java
class Solution {
    private Set<List<Integer>> visited=new HashSet();
    private Queue<List<Integer>> q=new LinkedList();
    public int minimumMoves(int[][] grid) {
        if(grid.length==0 || grid[0].length<2 || grid[0][0]!=0 || grid[0][1]!=0)
            return -1;
        int n=grid.length, m=grid[0].length;
        List<Integer> pos=new ArrayList();
        pos.add(0); pos.add(0); pos.add(0); pos.add(1);
        q.add(pos);
        visited.add(pos);
        int count=0;
        while(!q.isEmpty()){
            int len=q.size();
            while(len-->0){
                List<Integer> node=q.poll();
                if(node.get(0)==n-1 && node.get(1)==m-2 && node.get(2)==n-1 && node.get(3)==m-1)
                    return count;
                moveRight(grid, node,n,m);
                moveDown(grid, node,n,m);
                rotate1(grid, node,n,m);
                rotate2(grid, node,n,m);
            }
            count++;
        }
        return -1;
    }
    
    public void moveRight(int[][] grid, List<Integer> pos, int n, int m){
        List<Integer> next=new ArrayList(pos);
        next.set(1, next.get(1)+1);
        next.set(3, next.get(3)+1);
        if(!visited.contains(next) && next.get(3)<m && grid[next.get(0)][next.get(1)]==0 && grid[next.get(2)][next.get(3)]==0){
            visited.add(next);
            q.add(next);
        }
    }
    public void moveDown(int[][] grid, List<Integer> pos, int n, int m){
        List<Integer> next=new ArrayList(pos);
        next.set(0, next.get(0)+1);
        next.set(2,next.get(2)+1);
        if(next.get(0)<n && next.get(2)<n && grid[next.get(0)][next.get(1)]==0 && grid[next.get(2)][next.get(3)]==0 && !visited.contains(next)){
            visited.add(next);
            q.add(next);
        }
    }
    public void rotate1(int[][] grid, List<Integer> pos, int n, int m){
        List<Integer> next=new ArrayList(pos);
        next.set(2,next.get(2)+1);
        next.set(3, next.get(1));
        if(pos.get(3)>pos.get(1) && next.get(0)+1<n && grid[next.get(0)+1][next.get(1)]==0 && grid[pos.get(2)+1][pos.get(3)]==0&& !visited.contains(next)){
            visited.add(next);
            q.add(next);
        }  
    }
    
    public void rotate2(int[][] grid, List<Integer> pos, int n, int m){
        List<Integer> next=new ArrayList(pos);
        next.set(2, next.get(0));
        next.set(3, next.get(3)+1);

        if(pos.get(2)>pos.get(0) && pos.get(1)+1<m && grid[pos.get(0)][pos.get(1)+1]==0 && grid[pos.get(2)][pos.get(3)+1]==0 && !visited.contains(next)){
            visited.add(next);
            q.add(next);
        }
    }
}
```

## [542 01 Matrix](https://leetcode.com/problems/01-matrix/)

> Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

> The distance between two adjacent cells is 1.

We can using BFS traverse the matrix, like traverse the matrix layer by layer. 

Firstly we add add all the `0` into queue, and if the point is not `0`, set the distance to be max.

Then using BFS to set the distance, this time we will go through all the point next to `0`, whose distance will be 1, and then we will go through all the points next to 1, whose distance is 2, .....

The time complexity will be O(nm), the space complexity will be O(1) if we modify the origin matrix, otherwishe O(nm);

1. 之前潜意识 BFS 是从一个点出发，其实可以从一堆点出发，
2. 关于 Java 语言坐标如何加入队列

```Java
public class Solution {
    public int[][] updateMatrix(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        
        Queue<int[]> queue = new LinkedList<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == 0) {
                    queue.offer(new int[] {i, j});
                }
                else {
                    matrix[i][j] = Integer.MAX_VALUE;
                }
            }
        }
        
        int[][] dirs = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        
        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            for (int[] d : dirs) {
                int r = cell[0] + d[0];
                int c = cell[1] + d[1];
                if (r < 0 || r >= m || c < 0 || c >= n || 
                    matrix[r][c] <= matrix[cell[0]][cell[1]] + 1) continue;
                queue.add(new int[] {r, c});
                matrix[r][c] = matrix[cell[0]][cell[1]] + 1;
            }
        }
        
        return matrix;
    }
}
```