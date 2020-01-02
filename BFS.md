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

## [317 Shortest Distance from All Buildings](https://leetcode.com/problems/shortest-distance-from-all-buildings/)  :triangular_flag_on_post:

> You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

> - Each 0 marks an empty land which you can pass by freely.
> - Each 1 marks a building which you cannot pass through.
> - Each 2 marks an obstacle which you cannot pass through.

Traverse the matrix. For each building, use BFS to compute the shortest distance from each '0' to
this building. After we do this for all the buildings, we can get the sum of shortest distance
from every '0' to all reachable buildings. This value is stored
in 'distance[][]'. For example, if grid[2][2] == 0, distance[2][2] is the sum of shortest distance from this block to all reachable buildings.
Time complexity: O(number of 1)O(number of 0) ~ O(m^2n^2)

```Java
class Solution {
    public int shortestDistance(int[][] grid) {
        if(grid.length==0 || grid[0].length==0) return -1;
        int n=grid.length, m=grid[0].length;
        int[][] distence=new int[n][m];
        int[][] reach=new int[n][m];
        int[] dx={0,1,0,-1};
        int[] dy={1,0,-1,0};
        int buildings=0;
        for(int i=0; i<n; ++i){
            for(int j=0; j<m; ++j){
                if(grid[i][j]==1){
                    //BFS
                    buildings++;
                    Queue<int[]> q=new LinkedList();
                    boolean[][] visited=new boolean[n][m];
                    q.add(new int[]{i,j});
                    visited[i][j]=true;
                    int dis=1;
                    while(!q.isEmpty()){
                        int len=q.size();
                        for(int co=0; co<len; ++co){
                            int[] point=q.poll();
                            for(int k=0; k<4; ++k){
                                int nx=point[0]+dx[k];
                                int ny=point[1]+dy[k];
                                if(nx>=0 && nx<n && ny>=0 && ny<m && !visited[nx][ny]&& grid[nx][ny]==0){
                                    distence[nx][ny]+=dis;
                                    reach[nx][ny]++;
                                    q.add(new int[] {nx,ny});
                                    visited[nx][ny]=true;
                                }
                            }
                        }
                        dis++;
                    }
                }
            }
        }
        int ans=Integer.MAX_VALUE;
        for(int i=0; i<n; ++i){
            for(int j=0; j<m; ++j){
                if(grid[i][j]==0 && reach[i][j]==buildings){
                    ans=Math.min(distence[i][j], ans);
                }
            }
        }
        return ans==Integer.MAX_VALUE?-1:ans;
    }
}
```

## [490 The Maze](https://leetcode.com/problems/the-maze/)

> There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

> Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.

> The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.

标准 BFS 案例，记住 visited 不用需要用 set 保存！直接再用一个二维数组就可以了！

```Java
class Solution {
    public boolean hasPath(int[][] maze, int[] start, int[] destination) {
        int m=maze.length, n=maze[0].length;
        if(start[0]==destination[0] && start[1]==destination[1])    return true;
        int[][] dir=new int[][]{{0,1},{0,-1},{1,0},{-1,0}};
        // in 2d matrix graph, using 2d array to store the visited, 
        // no need to use set, idiot!
        boolean[][] visited=new boolean[m][n];
        Queue<Integer> X=new LinkedList();
        Queue<Integer> Y=new LinkedList();
        X.add(start[0]);
        Y.add(start[1]);
        visited[start[0]][start[1]]=true;
        while(!X.isEmpty()){
            int x=X.poll();
            int y=Y.poll();
            for(int i=0; i<4; ++i){
                int xx=x, yy=y;
                while(xx>=0 && xx<m && yy>=0 && yy<n && maze[xx][yy]==0){
                    xx+=dir[i][0];
                    yy+=dir[i][1];
                }
                xx-=dir[i][0];
                yy-=dir[i][1];
                if(visited[xx][yy]) continue;
                X.add(xx);
                Y.add(yy);
                visited[xx][yy]=true;
                if(xx==destination[0] && yy==destination[1])  return true;
            }
        }
        return false;
    }
}
```

## maze solver

> 给你一个二维数组，1 代表墙，0 代表通路，输出一个从起始位置到终止位置的路径

谷歌面试题，从起始位置到终止位置简单，BFS 和 DFS都可以，关键是怎么只输出一个路径，如果输入所有路径直接 DFS。

关于输出路径问题我们要做的就是记录当前点是从哪个点得到的。这里可以用一个三维数组 `lastPint[i][j][k]` 表示在位置`(i,j)`的点是从哪里来的。（妈的面试的 DP 问题也是三维数组，三维 DP）。

另外对于检查这种矩阵的 `visited`，可以另起一个二维boolean数组记录是否访问过，对于这个问题，如果可以更改原矩阵，可以直接将 0 改为 1.

```Java
import java.util.*;

class Untitled {
	public static void main(String[] args) {
		int[][] maze=new int[][]{{0,0,0,0},{1,1,0,0},{1,1,0,0},{1,0,0,1}};
		int[] start=new int[]{0,0};
		int[] end=new int[]{3,1};
		List<int[]> ans=findAPath(maze, start, end);
		for(int[] p: ans)
			System.out.println(p[0]+","+p[1]);
	}
	
	public static List<int[]> findAPath(int[][] maze, int[] start, int[] end){
		int m=maze.length, n=maze[0].length;
		int[][][] lastPoint=new int[m][n][2];
		for(int i=0; i<m; i++){
			for(int j=0; j<n; ++j){
				Arrays.fill(lastPoint[i][j], -1);
			}
		}
		// could we modify the maze matrix? 
		Queue<int[]> q=new LinkedList();
		q.add(start);
		maze[start[0]][start[1]]=1;
		int[][] dirs=new int[][]{{0,1},{0,-1},{1,0},{-1,0}};
		while(!q.isEmpty()){
			int[] curr=q.poll();
			int x=curr[0], y=curr[1];
			for(int[] dir: dirs){
				int nx=x+dir[0];
				int ny=y+dir[1];
				if(nx>=0 && nx<m && ny>=0 && ny<n && maze[nx][ny]==0){
					maze[nx][ny]=1;
					lastPoint[nx][ny][0]=x;
					lastPoint[nx][ny][1]=y;
					q.add(new int[]{nx, ny});
				}
			}
		}
		List<int[]> ans=new LinkedList<int[]>();
		if(lastPoint[end[0]][end[1]][0]==-1)	return ans;
		ans.add(end);
		int x=lastPoint[end[0]][end[1]][0];
		int y=lastPoint[end[0]][end[1]][1];
		while(x!=-1){
			ans.add(0,new int[]{x,y});
			int xx=x, yy=y;
			x=lastPoint[xx][yy][0];
			y=lastPoint[xx][yy][1];
		}
		return ans;
		
	}
}
```