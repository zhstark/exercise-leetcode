# ============================= No.543 =============================
# =================== DFS with Linked List Graph =============================
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

# ============================= Problem 200 =============================
# ============================= Number of Islands ========================
# 二维数组第一个下标是行，y 轴坐标，第二个下边是列，x 轴坐标
# 二维数组的边界问题，可以用函数处理，在最开始判断是否越界，迭代的时候 直接把四个方向全部输入就 ok，不用分多种情况
# 该题用二维数组遍历不行，还是得用图的算法
# 这种二维数组，只有 0，1 的可以通过换值（如‘#’）来做标记


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
