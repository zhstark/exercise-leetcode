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
