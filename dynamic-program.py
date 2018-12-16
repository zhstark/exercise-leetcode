# ===========================Problem 152==========================
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
