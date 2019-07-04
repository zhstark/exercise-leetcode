## [560 Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) :triangular_flag_on_post:

> Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Cumulating the sum. If `sum[j]-sum[i]=k`, the sum of elements lying between indices i and j is k.

But in this case, we have no need to store an array of sum but make full use of hashtable ~~which is used to store the cumulative sum upto all the indices possible along with the number of times the same sum occurs.~~ The key is `sum[i]`, the value is the number of `sum[i]` occurence. When we cumulated upto `sum[j]`, if `hash[sum[j]-k]=m`, we know that there are m times that a subarray with sum k has occured upto the current index. `count+=m`.

**corner case: what if `sum[j]=k`? So we insert {0:1} into the hashtable**

C++
```cpp
int subarraySum(vector<int>& nums, int k) {
    unordered_map<int, int> hashtable;
    int sj=0;
    int count=0;
    // Donot forget to insert 0
    hashtable[0]=1;
    for(int i=0; i<nums.size(); ++i){
        sj+=nums[i];
        if(hashtable.count(sj-k)!=0){
            count+=hashtable[sj-k];
        }
        if(hashtable.count(sj)==0)
            hashtable[sj]=1;
        else
            hashtable[sj]++;
    }
    return count;        
}
```

Java
```Java
class Solution {
    public int subarraySum(int[] nums, int k) {
        int count=0, sum=0;
        HashMap<Integer, Integer> map= new HashMap<>();
        map.put(0,1);
        for(int i=0; i<nums.length; ++i){
            sum+=nums[i];
            if(map.containsKey(sum-k))
                count+=map.get(sum-k);
            map.put(sum, map.getOrDefault(sum, 0)+1);
        }
        return count;
    }
}
```
## 325 Maximum Size Subarray Sum Equals k 

最开始没有用 hashtable，时间复杂度为 O(n^2)，超时。
HashTable 的优势在于检索时间为 O(1) 
这道题并不需要我去遍历运算，只需要 check 有没有
Si 为索引从 0-i 的和，则索引从 i-j的为 Si-Sj
问题解决类似于2sum

```py
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
```


## 311 Sparse Matrix Multiplication

松散矩阵有数据的位置少，所以可以使用 hashtable，不会过分占用空间，同时可以缩短时间

```py
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
```