二维矩阵，上下左右遍历移动的写法：

```python
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
for k in range(4):
    nx, ny = x + dx[k], y + dy[k]   
    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == (限制条件):
```
