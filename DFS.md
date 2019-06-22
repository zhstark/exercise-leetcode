## [1079 Letter Tile Possibilities](https://leetcode.com/problems/letter-tile-possibilities/)

> You have a set of tiles, where each tile has one letter tiles\[i\] printed on it.  Return the number of possible non-empty sequences of letters you can make.

C++:

```cpp
class Solution {
public:
    int numTilePossibilities(string tiles) {
        int chars[26] {0};
        // Counting, using it as a hashtable
        for(char c: tiles){
            chars[c-'A']++;
        }
        return dfs(chars);
    }
private:
    int dfs(int *chars){
        int s=0;
        
        // Since in this dfs, for this position, this for-loop will only get one character once, it avoids duplicating.
        for(int i=0; i<26; ++i){
            
            // Dont have this character, just pass
            if(chars[i]==0)
                continue;
            
            // count+1,  now s will be the answer if we just stop on this position.
            ++s;
            chars[i]--;
            s+=dfs(chars);
            chars[i]++;
        }
        return s;
    }
};
```

Java

```Java
// Explaination is in c++ code.
class Solution {
    public int numTilePossibilities(String tiles) {
        int[] chars=new int[26];
        for(char c: tiles.toCharArray()){
            chars[c-'A']++;
        }
        return dfs(chars);
    }
    
    private int dfs(int[] chars){
        int sum=0;
        for(int i=0; i<26; ++i){
            if(chars[i]==0) continue;
            sum++;
            chars[i]--;
            sum+=dfs(chars);
            chars[i]++;
        }
        return sum;
    }
}
```

## 543 

DFS with Linked List Graph 

Definition for a binary tree node.

Python:

```py
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
```

##   200 Number of Islands 

二维数组第一个下标是行，y 轴坐标，第二个下边是列，x 轴坐标

二维数组的边界问题，可以用函数处理，在最开始判断是否越界，迭代的时候 直接把四个方向全部输入就 ok，不用分多种情况

该题用二维数组遍历不行，还是得用图的算法

这种二维数组，只有 0，1 的可以通过换值（如‘#’）来做标记

Python:

```py
class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        r = len(grid)
        c = len(grid[0])
        count = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1':
                    self.dfs((i, j), r, c, grid)
                    count += 1

        return count

    def dfs(self, coordinate, r, c, grid):
        y, x = coordinate
        if y < 0 or x < 0 or y > r-1 or x > c-1:
            return

        if grid[y][x] == '1':
            grid[y][x] = '#'
            self.dfs((y-1, x), r, c, grid)
            self.dfs((y+1, x), r, c, grid)
            self.dfs((y, x-1), r, c, grid)
            self.dfs((y, x+1), r, c, grid)
```

