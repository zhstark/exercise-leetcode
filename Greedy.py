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


# ===========================Problem 253==========================
# =========== Meeting Rooms II =========
# 不能 in random order， 按照 start time 从小到大来安排 room
# 匿名函数 配 sorted 高阶函数
# 开始没有使用优先队列，而是遍历检查所有 room 的时间导致超时。
# 发现贪心算法经常和优先队列一起出现
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x.start)

        l = []
        heapq.heappush(l, intervals[0].end)
        for k in intervals[1:]:
            if l[0] <= k.start:
                heapq.heappop(l)
            heapq.heappush(l, k.end)
        return len(l)
