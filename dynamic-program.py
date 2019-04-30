# ===========================Problem 152==========================
# =========== Maximum Product Subarray =========
# 太他妈鸡儿南难了这题
# 局部最优与全局最优的关系
# 维护一个局部最优不行就维护两个，一个最大一个最小（因为两者会因为负号改变）

class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        ans = nums[0]
        localMax = nums[0]
        localMin = nums[0]
        for i in range(1, len(nums)):
            copyMax = localMax
            localMax = max(max(localMax*nums[i], nums[i]), nums[i]*localMin)
            localMin = min(min(copyMax*nums[i], nums[i]), nums[i]*localMin)
            ans = max(ans, localMax)

        return ans

# ============================= Problem 639 ===========================
# ============================= Decode Ways II ===========================
# =========== 下面有个简单级别的 ================
# 创建一个数组用来存储
# 分成两类解决：
# 1.新添加的只单个考虑，在一定条件下 f(n)=f(n-1)
# 2.结合上一个数组成一个两位数考虑，f(n)+=k*f(n-2) k与‘*’有关
# 这里的一个代码缺陷就是遍历时老是要考虑 i==1
# 下面另一道题的方案比较好，在遍历的时候指针为 i，计算考虑的是 i-1 和 i-2


class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if "00" in s or s[0] == "0" or not s:
            return 0

        dp = [0 for _ in range(len(s))]

        if s[0] == '*':
            dp[0] = 9
        else:
            dp[0] = 1
        for i in range(1, len(s)):
            if s[i] != '0' and s[i] != '*':
                dp[i] += dp[i-1]
            elif s[i] == '*':
                dp[i] += 9*dp[i-1]

            if s[i-1:i+1] > '09' and s[i-1:i+1] < '27' and s[i] != '*':
                if i != 1:
                    dp[i] += dp[i-2]
                else:
                    dp[i] += 1
            elif s[i-1] == '*':
                if s[i] >= '0' and s[i] < '7':
                    if i != 1:
                        dp[i] += 2*dp[i-2]
                    else:
                        dp[i] += 2
                elif s[i] != '*':
                    if i != 1:
                        dp[i] += dp[i-2]
                    else:
                        dp[i] += 1
                else:
                    if i != 1:
                        dp[i] += 15*dp[i-2]
                    else:
                        dp[i] += 15
            elif s[i] == '*':
                if s[i-1] == '1':
                    if i != 1:
                        dp[i] += 9*dp[i-2]
                    else:
                        dp[i] += 9
                elif s[i-1] == '2':
                    if i != 1:
                        dp[i] += 6*dp[i-2]
                    else:
                        dp[i] += 6
            if dp[i-1] > (10**9+7):
                dp[i-1] = dp[i-1] % (10**9+7)
                dp[i] = dp[i] % (10**9+7)
        return dp[len(s)-1] % (10**9+7)

# ============================= Problem 91 =============================
# =============== Decode ways =============================
# 最开始的判断其实没必要这么复杂
# 整体思路和上面一样，先考虑一个，再考虑两个的

class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or ('00' in s) or (s[0] == '0'):
            return 0

        dp = [0 for _ in range(len(s)+1)]
        dp[0] = 1

        for i in range(1, len(s)+1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            if i != 1 and s[i-2:i] > "09" and s[i-2:i] < "27":
                dp[i] += dp[i-2]

        return dp[len(s)]

# ============================= Problem 139 =============================
# ============================= Word Break =============================
# 发现很多 dp 问题都是有一个数组来对应保存每一步的结果。 （自底向上法）


class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False for _ in range(len(s))]

        for i in range(len(s)):
            for w in wordDict:
                if w == s[i-len(w)+1:i+1] and (dp[i-len(w)] or i-len(w) < 0):
                    dp[i] = True

        return dp[len(s)-1]

# ================================ Problem 188 ========================
# ===================== Best Time to Buy and Sell Stock IV =========
# 这道题难在找状态和状态转移方程。
# 另外 k大于n//2与不大于分开讨论。


class Solution:
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices or not k:
            return 0

        n = len(prices)

        if k >= n//2:
            s = 0
            for i in range(1, n):
                if prices[i] > prices[i-1]:
                    s = s+prices[i]-prices[i-1]
            return s

        dp = [[0 for _ in range(n)] for _ in range(k+1)]
        for x in range(1, k+1):
            temp = float("-inf")
            for i in range(1, n):
                temp = max(temp, dp[x-1][i-1]-prices[i-1])
                dp[x][i] = max(dp[x][i-1], prices[i]+temp)

        return dp[k][n-1]


# ================================ Problem 560 ========================
# ===================== Subarray Sum Equals K =========
# 思路差不多了，答案里有更简洁的代码细节。
class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0

        n = len(nums)
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        count = 0
        if dp[0] == k:
            count += 1
        for i in range(1, n):
            dp[i] = dp[i-1]+nums[i]
            if dp[i] == k:
                count += 1
        hashtable = {}
        for i in range(n):
            if dp[i]-k in hashtable:
                count += hashtable[dp[i]-k]

            if dp[i] not in hashtable:
                hashtable[dp[i]] = 1
            else:
                hashtable[dp[i]] += 1

        return count


# == == == == == == == == Problem 403 == == == == == == == == == == == ==
# ===================== frog jump =========
# 不再用数组，用 hashtable
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if not stones or (len(stones) > 1 and stones[1] != 1):
            return False

        dic = {}
        for i in stones:
            dic[i] = set()

        dic[1].add(1)

        for unit in stones:
            if unit == 0:
                continue

            for size in dic[unit]:
                if unit+size in dic:
                    dic[unit+size].add(size)
                if unit+size+1 in dic:
                    dic[unit+size+1].add(size+1)
                if size > 1 and (unit+size-1 in dic):
                    dic[unit+size-1].add(size-1)

        if not dic[stones[-1]]:
            return False
        else:
            return True

#============= 一个 string，返回最长的重复 string =========

def dynamic(s):
    if not s:
        return ""

    n=len(s)
    dp=[["" for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if s[i-1]==s[j-1] and i!=j:
                dp[i][j]=dp[i-1][j-1]+s[i-1]
                if len(dp[i][j])>len(ans):
                    ans=dp[i][j]
    return ans
                