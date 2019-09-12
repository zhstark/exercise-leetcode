拓扑排序需要使用图的数据结构来方便实现。
构建好图之后需要创建一个数组来记录各节点的入度。

## [269 Alien Dictionary](https://leetcode.com/problems/alien-dictionary/)  :triangular_flag_on_post:

> There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

我们将先后顺序看成一种依赖关系，即如果`r`在`w`后面就认为`r`依赖于`w`。那么这道题就是一道典型的拓扑排序。

我们用一个 hashmap 来表示图，key 为节点，value 为其连接的其他节点，那么这个 hashmap 的 key 设置为字符，value 设置为存储字符的 set。另外我们再用一个 hashmap 保存各个节点的入度。

这道题的思路就是

1. 初始化所有节点（字符）的入度为 0
2. 构建这个图，同时记录其入度。
3. 拓扑排序
4. 检查有没有环。在这个题检查环的依据是：最后输出的节点个数如果小于图中的节点个数，即图中还剩入度不为 0 的节点，那么就是有环

C++

```cpp
class Solution {
public:
    string alienOrder(vector<string>& words) {
        if(words.size()==0) return "";
        string result="";
        map<char, int> degree;
        map<char, set<char> > graph;
        for(auto word: words){
            for(auto c: word)
                degree[c]=0;
        }
        // build graph
        for(int i=0; i<words.size()-1; ++i){
            string curr=words[i];
            string next=words[i+1];
            int length=min(curr.size(), next.size());
            for(int j=0; j<length; ++j){
                char c1=curr[j];
                char c2=next[j];
                if(c1!=c2){
                    set<char> nodes;
                    if(graph.find(c1)==graph.end()){
                        nodes.insert(c2);
                        degree[c2]++;
                        graph[c1]=nodes;
                    }
                    else{
                        if(graph[c1].find(c2)==graph[c1].end()){
                            graph[c1].insert(c2);
                            degree[c2]++;
                        }
                    }
                    break;
                }
            }
        }
        queue<char> q;
        for(auto it: degree){
            if(it.second==0)
                q.push(it.first);
        }
        
        while(!q.empty()){
            char node=q.front();
            result+=node;
            q.pop();
            for(auto c: graph[node] ){
                degree[c]--;
                if(degree[c]==0)
                    q.push(c);
            }
        }
        cout<<result<<endl;
        if(degree.size()>result.size())
            return "";
        return result;
    }
};
```

Java

```Java
class Solution{
    public Stirng alienOrder(String[] words){
        if(words==null || words.length==0)  return "";
        Map<Character, Set<Character>> graph=new HashMap();
        Map<Character, Integer> degree=new HashMap();
        for(String word:words){
            for(char c: word.toCharArray()){
                degree.put(c, 0);
        }

        for(int i=0; i<words.length-1; ++i){
            String curr=words[i];
            String next=words[i+1];
            int length=Math.min(curr.length(), next.length())
            for(int j=0; j<length; ++j){
                char c1=curr.charAt(j);
                char c2=next.charAt(j);
                if(c1!=c2){
                    Set<Character> nodes=new HashSet();
                    if(graph.containsKey(c1))   nodes=graph.get(c1);
                    if(!nodes.contains(c2)){
                        nodes.add(c2);
                        graph.put(c1, nodes);
                        degree.put(c2, degree.get(c2)+1);
                    }
                    break;
                }
            }
        }
        StringBuilder result=new StringBuilder();
        Queue<Character> q=new LinkedList();
        for(char c: degree.keySet()){
            if(degree.get(c)==0)
                q.offer(c);
        }

        while(!q.isEmpty()){
            char c=q.poll();
            result.append(c);
            if(graph.containsKey(c)){
                for(char node: graph.get(c)){
                    degree.put(node, degree.get(node)-1);
                    if(degree.get(node)==0)
                        q.offer(node);
                }
            }
        }

        if(result.length()!=degree.size())  return "";
        return result.toString();
    }
}
```

## Problem 210 Course Schedule II 

```python
def Kahn2(self, numCourses, prerequisites):
        count = [0 for _ in range(numCourses)]
        dic = {}  # 构建一个图， key 为顶点，value 为链接点，用于检测环
        ans = []
        for i in range(len(prerequisites)):
            course = prerequisites[i][0]
            count[course] += 1
            v = prerequisites[i][1]
            if course in dic and v in dic[course]:
                return []
            if v not in dic:
                dic[v] = [course]
            else:
                dic[v].append(course)

        q = collections.deque([])
        for i in range(len(count)):
            if count[i] == 0:
                q.append(i)
        while q:
            v = q.popleft()
            ans.append(v)
            if v in dic:
                for u in dic[v]:
                    count[u] -= 1
                    if count[u] == 0:
                        q.append(u)
                dic.pop(v)

        if len(ans) != numCourses:
            return []
        return ans
```