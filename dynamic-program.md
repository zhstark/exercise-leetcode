
## 0-1 knapsack

对于一组不同重量，不同价值，不可分割的物品，我们选择将某些物品装入背包，在满足背包最大重量限制的条件下，背包可装入的最大总价值是多少？

Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.

`n: number of items`
`w: maximum weight of the knapscak`

set a 2 dimension matrix `states[n][w+1]`, `states[i][j]` means when we decide item i, now the weight is j, the max value is `states[i][j]`

`states[i][j]=max( states[i-1][j], states[i][j],states[i-1][ j-weight[i] ]+v[i]), ( j-weight[i]>=0 )`

```cpp
int knapscak(vector<int> A, vector<int> values, int w){
    int n=A.size();
    vector<vector<int> > dp(n, vector<int>(w+1, 0));
    int m=0;
    if(A[0]<=w)
        dp[0][A[0]]=values[0];
    for(int i=1; i<n; ++i){
        for(int j=0; j<=w; ++j){
            dp[i][j]=max(dp[i][j],dp[i-1][j]);
            if(j-A[i]>=0)
                dp[i][j]=max( dp[i][j], dp[i-1][j-A[i]]+values[i] );
            m=max(m,dp[i][j]);
        }
    }
    return m;
}
```

## Problem 152 Maximum Product Subarray 

 太他妈鸡儿南难了这题
 局部最优与全局最优的关系
 维护一个局部最优不行就维护两个，一个最大一个最小（因为两者会因为负号改变）

```py
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
```


##  Problem 639  Decode Ways II 

下面有个简单级别的 
 
创建一个数组用来存储,分成两类解决：
 
1.新添加的只单个考虑，在一定条件下 f(n)=f(n-1)
2.结合上一个数组成一个两位数考虑，f(n)+=k*f(n-2) k与‘*’有关
 
这里的一个代码缺陷就是遍历时老是要考虑 i==1
 
下面另一道题的方案比较好，在遍历的时候指针为 i，计算考虑的是 i-1 和 i-2

```py
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
```

##  Problem 91  Decode ways 

 最开始的判断其实没必要这么复杂
 
 整体思路和上面一样，先考虑一个，再考虑两个的

```py
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
```

## Problem 139  Word Break 

 发现很多 dp 问题都是有一个数组来对应保存每一步的结果。 （自底向上法）

```py
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
```

## Problem 188  Best Time to Buy and Sell Stock IV 

这道题难在找状态和状态转移方程。
 
另外 k大于n//2与不大于分开讨论。

```py
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
```

## Problem 560  Subarray Sum Equals K 

思路差不多了，答案里有更简洁的代码细节。

```py
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
```

## Problem 403 frog jump 

 不再用数组，用 hashtable

```py
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
```


## 一个 string，返回最长的重复 string 

```py

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
                
```

## [343 Integer Break](https://leetcode.com/problems/integer-break/)

Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

Botttom-up. When n<=1, f(n)=0; when n=2, f(n)=1\*1=1; when n=3, f(n)=2\*1=2; when n=4, f(n)=2\*2=4. Start from 4， f(n)>n.

So when n>3, f(n)=max(f(i)\*f(n-i)), in which f(1)=1,f(2)=2,f(3)=3.

```cpp

class Solution {
public:
    int integerBreak(int n) {
        if(n<=1)    return -1;
        
        vector<int> dp(n+1,1);
        if(n<2) return 0;
        if(n==2)    return 1;
        if(n==3)    return 2;
        dp[0]=0;
        dp[1]=1;
        dp[2]=2;
        dp[3]=3;
        for(int i=4;i<=n; ++i){
            for(int j=1; j<=i/2; ++j){
                dp[i]=max(dp[i], dp[j]*dp[i-j]);
            }
        }
        return dp[n];
    }
};
```


## [474 Ones and Zeroes](https://leetcode.com/problems/ones-and-zeroes/)

> In the computer world, use restricted resource you have to generate maximum benefit is what we always want to pursue.

> For now, suppose you are a dominator of m 0s and n 1s respectively. On the other hand, there is an array with strings consisting of only 0s and 1s.

> Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s. Each 0 and 1 can be used at most once.

The key for dp problems is to find the states. In this case, we wanna use a 3 dimension matrix `states[i][m][n]` denoting that when I consider `ith` element, `states[i][m][n]` is the maximum number of strings than I can form with **m** `0s` and **n** `1s`.

Then `states[i][m][n]=max(states[i-1][m-m_i][n-n_i]+1, states[i-1][m][n]`.

But 3 dimension is too complex. We can just use a 2 dimension maxtrix traversing `l` times, `l` is the number of elements.

For each element in the given array, updating a 2 dimension matrix `dp[i][j]`, `dp[i][j]` is the max number of string for now, having **i** `0s` and **j** `1s` left unused.

**When updating `dp`, we have to go from botton-right to top-left. Because otherwise we will overcounting.**

```cpp

class Solution {
public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        if(strs.size()==0)  return 0;
        int count=0;
        vector<vector<int> > dp(m+1, vector<int>(n+1, 0));
        int ans=0;
        for(auto str:strs){
            int t0=0, t1=0;
            for(auto c:str){
                if(c=='0')  ++t0;
                else if(c=='1') ++t1;
            }
            for(int i=m; i>=0; --i){
                for(int j=n; j>=0; --j){
                    if(i-t0>=0 && j-t1>=0){
                        dp[i][j]=max(1+dp[i-t0][j-t1], dp[i][j]);
                        ans=max(ans, dp[i][j]);
                    }
                }
            }
        }
        return ans;
    }
};

```