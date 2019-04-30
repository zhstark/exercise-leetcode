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