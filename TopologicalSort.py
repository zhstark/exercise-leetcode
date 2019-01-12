# ============================== Problem 210========================
# =================== Course Schedule II ================


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
