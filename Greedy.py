# ===========================Problem 621==========================
# =========== Task Scheduler =========
# trick 是通过维护 max heap 保持数组的排序
# 将字母转换为 int 的方式：int(xxx-'A')
# Python 库里没有最大堆，heapq 为最小堆，通过乘以-1将最大变为最小
import heapq

class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if not tasks:
            return 0

        h = []
        count = 0
        dic = collections.Counter(tasks)
        for i in dic.values():
            heapq.heappush(h, -i)

        while h:
            i = 0
            temp = []
            while i <= n:
                if not h and not temp:
                    break
                if h:
                    t = heapq.heappop(h)+1
                    if t < 0:
                        temp.append(t)
                count += 1
                i += 1

            for x in temp:
                heapq.heappush(h, x)

        return count
