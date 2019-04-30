## 二维矩阵，上下左右遍历移动的写法：

```python
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
for k in range(4):
    nx, ny = x + dx[k], y + dy[k]   
    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == (限制条件):
```

## 对角线从下向上填表

```py
for d in range(1,n):    #distance
    for i in range(n-d):
        j=i+d
        dp[i][j]=max(p[i]-dp[i+1][j], p[j]-dp[i][j-1])

```

## 不碰壁不能转向

```C++
void dfs(vector<vector<int>>& maze, pair<int,int> start, vector<vector<int>>& dis)
{
        int dx[4]={1,0,-1,0};
        int dy[4]={0,1,0,-1};
        for(int k=0;k<4;k++)
        {
            int x=start.first+dx[k];
            int y=start.second+dy[k];
            int count=0;
            while(x>=0 && y>=0 &&x<maze.size() && y<maze[0].size() && maze[x][y]==0)
            {
                x+=dx[k];
                y+=dy[k];
                count++;
            }
            x-=dx[k];
            y-=dy[k];
            if(dis[start.first][start.second]+count<dis[x][y])
            {
                dis[x][y]=dis[start.first][start.second]+count;
                dfs(maze, {x,y}, dis);
            }
        }
}
```