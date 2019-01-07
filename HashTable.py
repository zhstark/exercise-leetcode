# ===========================Problem 325==========================
# =========== Maximum Size Subarray Sum Equals k =========
# 最开始没有用 hashtable，时间复杂度为 O(n^2)，超时。
# HashTable 的优势在于检索时间为 O(1) 
# 这道题并不需要我去遍历运算，只需要 check 有没有
# Si 为索引从 0-i 的和，则索引从 i-j的为 Si-Sj
# 问题解决类似于2sum


class Solution:
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0

        n = len(nums)
        maxlength = 0
        s = 0
        dic = {}
        for i in range(n):
            s = s+nums[i]
            if s == k:
                maxlength = i+1
            elif s-k in dic:
                maxlength = max(maxlength, i+1-dic[s-k])
            if s not in dic:
                dic[s] = i+1

        return maxlength

# ===========================Problem 311==========================
# =========== Sparse Matrix Multiplication =========
# 松散矩阵有数据的位置少，所以可以使用 hashtable，不会过分占用空间，同时可以缩短时间


class Solution:
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        r = len(A)
        c = len(B[0])
        ans = [[0 for _ in range(c)] for _ in range(r)]

        n = len(B)
        dA, dB = {}, {}
        for i in range(r):
            for j in range(n):
                if A[i][j] != 0:
                    dA[(i+1, j+1)] = A[i][j]

        for i in range(n):
            for j in range(c):
                if B[i][j] != 0:
                    dB[(i+1, j+1)] = B[i][j]

        for r, c in dA.keys():
            for k in range(1, n+1):
                if (c, k) in dB:
                    ans[r-1][k-1] += A[r-1][c-1]*B[c-1][k-1]

        return ans
