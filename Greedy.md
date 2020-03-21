## [621 Task Scheduler](https://leetcode.com/problems/task-scheduler/) :triangular_flag_on_post: 

> Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

> However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

> You need to return the least number of intervals the CPU will take to finish all the given tasks.

问题可以转化为求解最少的 idle，那么最终结果就是 idle 的数目加上任务的总数。

最多次数的任务决定了一个框架，假设 A 最多，有 4 个，假设n=4，那么我们最后的结构一定是这样的（X 表示idle）：

```
AXXXX
AXXXX
AXXXX
A
```

之后要做的就是填补 X。此时`number_of_X = n * (number_of_A - 1)`

那么按照任务次数从多到少的顺序，将任务依次填入进去就好了，即`idle_slots=idle_slots-count[i]`，但此时注意，如果有任务的次数跟最多的一样，那么要减的不是 `count[i]`，而是`count[i]-1`。因为框架最后一行随便填，没有 idle。所以`idle_slots=idle_slots- min(count[i], max_val)`（`max_val`为最多的次数-1)

当然，也有可能最后不会有 idle，比如 n=4 时，任务很多，如下种情况，

```
ABCDEF
ABCDEG
ABCDS
AB
```

此时按照上述算法，idle_slots最终小于 0，所以最后 return 的时候要判断一下。

写代码的时候变量名经常忘记加 s，要注意一下。

C++
```cpp
class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        int count[26]={0};
        // counting the number
        for(auto ch: tasks){
            count[ch-'A']+=1;
        }
        sort(count, count+26);
        int max_val=count[25]-1;
        int idle_slots=n*max_val;
        for(int i=24; i>=0; --i){
            idle_slots-=min(count[i], max_val);
        }       
        return idle_slots> 0? idle_slots+tasks.size():tasks.size();      
    }
};
```

Java
```Java
class Solution {
    public int leastInterval(char[] tasks, int n) {
        //记得加 s
        int[] counts=new int[26];
        for(char c: tasks){
            counts[c-'A']++;
        }
        Arrays.sort(counts);
        int max_val=counts[25]-1;
        int idle_slots=n*max_val;
        for(int i=24; i>=0; --i){
            idle_slots-=Math.min(counts[i], max_val);
        }
        return idle_slots>0?idle_slots+tasks.length:tasks.length;
    }
}
```

## Problem 253 Meeting Rooms II 

不能 in random order， 按照 start time 从小到大来安排 room

匿名函数 配 sorted 高阶函数

开始没有使用优先队列，而是遍历检查所有 room 的时间导致超时。

发现贪心算法经常和优先队列一起出现

```py
#Definition for an interval.
#class Interval:
#    def __init__(self, s=0, e=0):
#        self.start = s
#        self.end = e

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
```

## [53 Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

> Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Keep adding the number into the sum, if the sum is smaller than 0, it means we need to have a new start.

```Java
class Solution {
    public int maxSubArray(int[] nums) {
        if(nums.length==0)  return 0;
        int maxNum=nums[0];
        int sum=nums[0];
        for(int i=1; i<nums.length;++i){
            if(sum>0)
                sum+=nums[i];
            else
                sum=nums[i];
            maxNum=Math.max(maxNum, sum);
        }
        return maxNum;
    }
}
```

## [1383 Maximum Performance of a Team](https://leetcode.com/problems/maximum-performance-of-a-team/) :green_book: 

> There are n engineers numbered from 1 to n and two arrays: speed and efficiency, where speed[i] and efficiency[i] represent the speed and efficiency for the i-th engineer respectively. Return the maximum performance of a team composed of at most k engineers, since the answer can be a huge number, return this modulo 10^9 + 7.

> The performance of a team is the sum of their engineers' speeds multiplied by the minimum efficiency among their engineers. 

Performance=sm(speed)*min(efficiency). Idea is simple: try every efficiency value from heighest to lowest and at the same time maintain an as-large-as-possible speed group, keep adding speed to total speed, if size of engineers group exceeds K, lay off the engineer with lowest speed.

1. Sort efficiency with descending order. Bacause, afterwards, when we iterate whoe engineers, every round, when calculating the current performance, minimum efficiency is the effiency of the new incoming engineer.
2. Maintain a pq to track of the minimum speed in the group. If size of group is K, kick the engineer with minimum speed out (since efficiency is fixed by new coming engineer, the only thing matters now is sum of speed).
3. Calculate/Update performance

I record 2 kinds of programming style to reference.

```Java
// This solution using inner class and override 
class Solution {
    private static final int MOD = 1000000007;
    
    public int maxPerformance(int n, int[] speed, int[] efficiency, int k) {
        Engineer[] E = new Engineer[n];
        for (int i = 0; i < n; ++i) {
            E[i] = new Engineer(speed[i], efficiency[i]);
        }
        Arrays.sort(E, Collections.reverseOrder(Engineer.BY_EFFICIENCY));
        
        long speedSum = 0;
        long best = 0;
        PriorityQueue<Long> topSpeeds = new PriorityQueue<>();
        for (Engineer e : E) {
            topSpeeds.add(e.speed);
            speedSum += e.speed;
            while (topSpeeds.size() > k) {
                long removeSpeed = topSpeeds.poll();
                speedSum -= removeSpeed;
            }
            best = Math.max(best, e.efficiency * speedSum);
        }
        return (int)(best % MOD);
    }
    
    private static class Engineer {
        public long speed, efficiency;
        
        public Engineer(long s, long e) {
            speed = s;
            efficiency = e;
        }
        
        public static final Comparator<Engineer> BY_EFFICIENCY = new Comparator<Engineer>() {
            @Override
            public int compare(Engineer lhs, Engineer rhs) {
                return Long.compare(lhs.efficiency, rhs.efficiency);
            }
        };
    }
}

----
int MOD = (int) (1e9 + 7);
int[][] engineers = new int[n][2];
for (int i = 0; i < n; ++i) 
	engineers[i] = new int[] {efficiency[i], speed[i]};

Arrays.sort(engineers, (a, b) -> b[0] - a[0]);

PriorityQueue<Integer> pq = new PriorityQueue<>(k, (a, b) -> a - b);
long res = Long.MIN_VALUE, totalSpeed = 0;

for (int[] engineer : engineers) {
	if (pq.size() == k) totalSpeed -= pq.poll();  // layoff the one with min speed
	pq.add(engineer[1]);
	totalSpeed = (totalSpeed + engineer[1]);
	res = Math.max(res, (totalSpeed * engineer[0]));  // min efficiency is the efficiency of new engineer
}

return (int) (res % MOD);
```


## [759 Employee Free Time](https://leetcode.com/problems/employee-free-time/)