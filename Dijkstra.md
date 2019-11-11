单源最短路径，从一个源点到其他所有点的最短距离。该算法假设所有的边权重为非负值（Bellman-Ford 算法可以检测权重为负数的环路）

## [505 The Maze II](https://leetcode.com/problems/the-maze-ii/

> There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

> Given the ball's start position, the destination and the maze, find the shortest distance for the ball to stop at the destination. The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included). If the ball cannot stop at the destination, return -1.

> The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.

Dijkstra 算法，注意是有权图。算一个点到所有点的最短路径。

在 Java 的优先级队列中，若要往里加匿名函数，注意实例化时的`<>`不能省略。

```Java
class Solution {
    private int[][] dirs=new int[][]{{0,1},{0,-1},{1,0},{-1,0}};
    public int shortestDistance(int[][] maze, int[] start, int[] dest) {
        int[][] distance=new int[maze.length][maze[0].length];
        for(int[] row: distance){
            Arrays.fill(row, Integer.MAX_VALUE);
        }
        distance[start[0]][start[1]]=0;
        dijkstra(maze, start, distance);
        return distance[dest[0]][dest[1]]==Integer.MAX_VALUE? -1:distance[dest[0]][dest[1]];
    }
    
    public void dijkstra(int[][] maze, int[] start, int[][] distance){
        PriorityQueue<int[]> pq=new PriorityQueue<>((a,b)->a[2]-b[2]);
        pq.add(new int[]{start[0],start[1],0});
        while(!pq.isEmpty()){
            int[] s=pq.poll();
            if(distance[s[0]][s[1]]<s[2])
                continue;
            for(int[] dir:dirs){
                int x=s[0]+dir[0];
                int y=s[1]+dir[1];
                int count=0;
                while(x>=0 && y>=0 && x<maze.length && y<maze[0].length && maze[x][y]==0){
                    x+=dir[0];
                    y+=dir[1];
                    count++;
                }
                x-=dir[0];
                y-=dir[1];
                if(distance[s[0]][s[1]]+count<distance[x][y]){
                    distance[x][y]=distance[s[0]][s[1]]+count;
                    pq.add(new int[]{x,y,distance[x][y]});
                }
            }
        }
    }
}
```


---- 

```python
# 743
class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """

        def BellmenFord(times, N, K):
            graph={}
            for u, v, w in times:
                if u not in graph:
                    graph[u]=[(v, w)]
                else:
                    graph[u].append((v, w))

            dist={node: float('inf') for node in range(1,N+1)}
            dist[K]=0

            def Relax(u,v,w):
                if dist[v]>dist[u]+w:
                    dist[v]=dist[u]+w

            for _ in range(N-1):
                for i in graph:
                    for v, w in graph[i]:
                        Relax(i,v, w)

            ans=max(dist.values())
            return ans if ans < float('inf') else -1

        def Dijkstra(times, N, K):
                graph=collections.defaultdict(list)
                for u, v, w in times:
                    graph[u].append((v,w))

                q=[(0, K)]
                # for key, dis in dist.items():
                #     heapq.heappush(q, (dis, key))
                def Relax(u,v,w):
                    if dist[v]>dist[u]+w:
                        dist[v]=dist[u]+w
                dist={node: float('inf') for node in range(1,N+1)}
                dist[K]=0
                seen=set()
                while q!=[]:
                    d, u=heapq.heappop(q)
                    if u in seen: continue
                    seen.add(u)
                    for v, w in graph[u]:
                        Relax(u,v,w)
                        heapq.heappush(q,(dist[v], v))

                ans=max(dist.values())
                return ans if ans<float('inf') else -1

        return Dijkstra(times, N, K)
```