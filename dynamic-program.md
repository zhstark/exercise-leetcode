<!-- GFM-TOC -->
- Content
  - [0-1 knapsack](#0-1-knapsack)
  - [Longset common substring](#Longset-common-substring)
  - [1092 Shortest Common Supersequence](#1092-Shortest-Common-Supersequence)
  - [1105 Filling Bookcase Shelves](#1092-Shortest-Common-Supersequence)
  - [322 Coin Change](#322-Coin-Change)
  - [152 Maximum Product Subarray](#152-Maximum-Product-Subarray)
  - [639 Decode Ways II](#639-Decode-Ways-II)
  - [91 Decode ways](#91-Decode-ways)
  - [139 Word Break](#139-Word-Break)
  - [188 Best Time to Buy and Sell Stock IV](#188-Best-Time-to-Buy-and-Sell-Stock-IV)
  - [560 Subarray Sum Equals K](#560-Subarray-Sum-Equals-K)
  - [403 frog jump](#403-frog-jump)
  - [343 Integer Break](#343-Integer-Break)
  - [474 Ones and Zeroes](#474-Ones-and-Zeroes)
  - [1027 Longest Arithmetic Sequence](#1027-Longest-Arithmetic-Sequence)  :triangular_flag_on_post:
  - [123 Best Time to Buy and Sell Stock III](#123-best-time-to-buy-and-sell-stock-iiihttpsleetcodecomproblemsbest-time-to-buy-and-sell-stock-iii)
  - [518 Coin Change 2](#518-coin-change-2httpsleetcodecomproblemscoin-change-2)
  - [309 Best Time to Buy and Sell Stock with Cooldown](#309-best-time-to-buy-and-sell-stock-with-cooldownhttpsleetcodecomproblemsbest-time-to-buy-and-sell-stock-with-cooldown)
  - [10 Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/)

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

## Longset common substring

最长公共子序列，这里子序列不一定在父字符串中是连续的。返回长度或字符串。

`dp[i][j]`表示字符串 `A[0:i+1]` 与 `B[0:j+1]` 中的最长公共子序列。

`dp[i][j]=0,  if i=0 or j=0;`
`dp[i][j]=dp[i-1][j-1]+1,  if i>0,j>0 and Ai=Bj;`
`dp[i][j]=max( dp[i][j-1], dp[i-1][j]),  if i,j>0 and Ai!=Bj`

C++

```cpp
// Return the string
string lcs(string& A, string& B){
    int n=A.size(), m=B.size();
    vector<vector<string>> dp(n+1, vector<string>(m+1, ""));
    for(int i=0; i<n; ++i){
        for(int j=0; j<m; ++j){
            if(A[i]==B[j])
                dp[i+1][j+1]=dp[i][j]+A[i];
            else
                dp[i+1][j+1]=dp[i+1][j].size()>dp[i][j+1].size()? dp[i+1][j]:dp[i][j+1];
        }
    }
    return dp[n][m];
}

// Return the length
int lcs_length(string& A, string& B){
    int n=A.size(), m=B.size();
    vector<vector<int>> dp(n+1, vector<int>(m+1, 0));
    for(int i=0; i<n; ++i){
        for(int j=0; j<m; ++j){
            if(A[i]==B[j])
                dp[i+1][j+1]=dp[i][j]+1;
            else
                dp[i+1][j+1]=dp[i+1][j]>dp[i][j+1]?dp[i+1][j]:dp[i][j+1];
        }
    }
    return dp[n][m];
}
```

## [1092 Shortest Common Supersequence](https://leetcode.com/problems/shortest-common-supersequence/)

> Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences.  If multiple answers exist, you may return any of them.

> (A string S is a subsequence of string T if deleting some number of characters from T (possibly 0, and the characters are chosen anywhere from T) results in the string S.)

Firstly, we need to find the longgest common substring(lcs), then we check which characters are missed in parent string.

When getting the answer using lcs, we set 2 pointers points to a parent string respectively. 

Then traversing lcs, let's say we are passing `ch`, for one parent string, if the character at index `i` is not equal to `ch`, we will add it to the answer and move the pointer forward. When both pointers point to character `ch`, now we have assembled all characters before `ch`, so we add `ch` now, and move 2 pointers forward one step.

When we traversed lcs, we add all the characters left in parent-strings.

C++

```cpp
class Solution {
public:
    string shortestCommonSupersequence(string str1, string str2) {
        int i=0, j=0;
        int n=str1.size(), m=str2.size();
        
        string res="";
        for(auto c: lcs(str1, str2)){
            while(i<n && str1[i]!=c)
                res+=str1[i++];
            while(j<m && str2[j]!=c)
                res+=str2[j++];
            res+=c;
            ++i;
            ++j;
        }
        return res+str1.substr(i)+str2.substr(j);
    }
    
private:
    string lcs(string& A, string& B){
        int n=A.size(), m=B.size();
        vector<vector<string>> dp(n+1, vector<string>(m+1, ""));
        for(int i=0; i<n; ++i){
            for(int j=0; j<m; ++j){
                if(A[i]==B[j])
                    dp[i+1][j+1]=dp[i][j]+A[i];
                else
                    dp[i+1][j+1]=dp[i+1][j].size()>dp[i][j+1].size()? dp[i+1][j]:dp[i][j+1];
            }
        }
        return dp[n][m];
    }
};
```

Java

```Java
class Solution {
    public String shortestCommonSupersequence(String A, String B) {
        // set 2 pointers, one points to A, the other points to B
        int i=0, j=0;
        StringBuilder res=new StringBuilder();
        // traverse the lcs
        String ll=lcs(A,B);
        for(int k=0; k<ll.length(); ++k){
            while(A.charAt(i)!=ll.charAt(k))
                res.append(A.charAt(i++));
            while(B.charAt(j)!=ll.charAt(k))
                res.append(B.charAt(j++));
            
            res.append(ll.charAt(k));
            ++i;
            ++j;
        }
        res.append(A.substring(i)).append(B.substring(j));
        return res.toString();
    }
    private String lcs(String A, String B){
        int n=A.length(), m=B.length();
        String[][] dp= new String[n+1][m+1];
        for(int i=0; i<=n; ++i)
            dp[i][0]="";
        for(int j=0; j<=m; ++j)
            dp[0][j]="";
        
        for(int i=0; i<n; ++i){
            for(int j=0; j<m; ++j){
                if(A.charAt(i)==B.charAt(j))
                    dp[i+1][j+1]=dp[i][j]+A.charAt(i);
                else
                    dp[i+1][j+1]=dp[i+1][j].length()>dp[i][j+1].length()?dp[i+1][j]:dp[i][j+1];
            }
        }
        return dp[n][m];
    }
}
```

## [1105 Filling Bookcase Shelves](https://leetcode.com/problems/filling-bookcase-shelves/)

> We have a sequence of books: the i-th book has thickness books\[i\]\[0\] and height books\[i\]\[1\].

> We want to place these books in order onto bookcase shelves that have total width shelf_width.

> We choose some of the books to place on this shelf (such that the sum of their thickness is <= shelf_width), then build another level of shelf of the bookcase so that the total height of the bookcase has increased by the maximum height of the books we just put down.  We repeat this process until there are no more books to place.

> Note again that at each step of the above process, the order of the books we place is the same order as the given sequence of books.  For example, if we have an ordered list of 5 books, we might place the first and second book onto the first shelf, the third book on the second shelf, and the fourth and fifth book on the last shelf.

> Return the minimum possible height that the total bookshelf can be after placing shelves in this manner.

Consider `dp[i]` as the minumum height up to the ith book, the `i+1`th book has two option:

1. Place it on another level. then `dp[i+1]=dp[i]+h[i+1]`;
2. Place it together with other books. Then `dp[i+1]=min(dp[j]+max(h[j+1] ... h[i]))`, where `sum(w[j+1]...w[i])<shelf_width`. This means `j+1`th book to `i+1`th book make up a level.

`dp[i+1]=min( option1, option2)`

```cpp
class Solution {
public:
    int minHeightShelves(vector<vector<int>>& books, int shelf_width) {
        int n=books.size();
        vector<int> dp( n+1, INT_MAX);
        dp[0]=0;
        for(int i=0; i<n; ++i){
            auto book=books[i];
            int w=book[0];
            int h=book[1];
            // option 1
            dp[i+1]=dp[i]+h;
            // option 2
            for(int j=i-1; j>=0; --j){
                w+=books[j][0];
                h=max(h ,books[j][1]);
                if(w>shelf_width)   break;
                dp[i+1]=min(dp[i+1], dp[j]+h);
            }
        }
        return dp[n];
    }
};
```

## [322 Coin Change](https://leetcode.com/problems/coin-change/)

> You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Think in dp method. If now we have all solutions for `amount<a`, when `amount=a`, we traverse all the coins, if `a-coins[i]` in `[0, amount]`, `dp[a]=min(dp[a-coins[i]]+1, dp[a])`. Now 

Time complexity: O(S\*n), where S is the amount, n is the denomination count. On each step, we get *F(i)* in n iterations.

Space complexity:O(S)

C++

```cpp
    int coinChange(vector<int>& coins, int amount) {
        int n=coins.size();
        if(n==0)    return -1;
        
        const int m=amount+1;
        int dp[amount+1];
        fill(dp, dp+amount+1, m);
        dp[0]=0;

        for(int i=1; i<=amount; ++i){
            for(auto c:coins){
                if(c<=i){
                    dp[i]=min(dp[i], dp[i-c]+1);
                }
            }
        }
        return dp[amount]>amount?-1:dp[amount];
    }
```

Java

```Java
class Solution {
    public int coinChange(int[] coins, int amount) {
        final int n=coins.length;
        int[] dp=new int[amount+1];
        int max=amount+1;
        Arrays.fill(dp, max);
        dp[0]=0;
        for(int i=1; i<=amount; ++i){
            for(int j=0; j<n; ++j){
                if(coins[j]<=i){
                    dp[i]=Math.min(dp[i], dp[i-coins[j]]+1);
                }
            }
        }
        return dp[amount]>=max?-1:dp[amount];
    }
}
```

## 152 Maximum Product Subarray 

 太他妈鸡儿南难了这题
 局部最优与全局最优的关系
 维护一个局部最优不行就维护两个，一个最大一个最小（因为两者会因为负号改变）

Python
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

Java
```Java
class Solution {
    public int maxProduct(int[] nums) {
        if(nums.length==0)  return 0;
        int r=nums[0];
        int imax=r;
        int imin=r;
        for(int i=1; i<nums.length; ++i){
            if(nums[i]<0){
                int temp=imax;
                imax=imin;
                imin=temp;
            }
                
            imax=Math.max(nums[i], imax*nums[i]);
            imin=Math.min(nums[i], imin*nums[i]);
            r=Math.max(r, imax);
        }
        return r;
    }
}
```

## 639 Decode Ways II 

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

## 91 Decode ways 

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

## 139 Word Break

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

## 188 Best Time to Buy and Sell Stock IV 

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

## 560 Subarray Sum Equals K 

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

## 403 frog jump 

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


## 一个 string 返回最长的重复 string 

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

## [1027 Longest Arithmetic Sequence](https://leetcode.com/problems/longest-arithmetic-sequence/)   :triangular_flag_on_post:

>  Given an array A of integers, return the length of the longest arithmetic subsequence in A.

> Recall that a subsequence of A is a list `A[i_1], A[i_2], ..., A[i_k]` with` 0 <= i_1 < i_2 < ... < i_k <= A.length - 1`, and that a sequence B is arithmetic if` B[i+1] - B[i] `are all the same value (for `0 <= i < B.length - 1`).

可太难了这题，咋能想到用 hashmap 的 list

We iteratively build the map for a new index i, by considering all elements to the left one-by-one.

For each pair of indices `(j,i) j<i` and difference `d=A[i]-A[j]`, we check if there was an existing chain at the index `j` with different `d` already.

```Java
class Solution {
    public int longestArithSeqLength(int[] A) {
        if(A.length==0) return 0;
        Map<Integer, Integer>[] dp=new HashMap[A.length];
        int ans=1;
        for(int i=0; i<A.length; ++i){
            dp[i]=new HashMap();
        }
        for(int i=1; i<A.length; ++i){
            int x=A[i];
            for(int j=0; j<i; ++j){
                int y=A[j];
                int d=x-y;
                int len=2;
                if(dp[j].containsKey(d))
                    len=dp[j].get(d)+1;
                //dp[i].put(d, dp[i].getOrDefault(d,0)+len);
                dp[i].put(d, len);
                ans=Math.max(ans, len);
            }
        }
        return ans;
    }
}
```

## [714 Best Time to Buy and Sell Stock with Transaction Fee](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)

> Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i; and a non-negative integer fee representing a transaction fee.

> You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction. You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)

> Return the maximum profit you can make.

dp 问题的关键是找状态，对这个题我们可以定义两个数组代表两个状态：

- `buy[]`代表在买入状态下，第 i 天的最大收益
- `sell[]`代表在卖出状态下，第 i 天的最大收益

那么在第 i 天，我们有三种可能：买入，啥也不干，卖出。在买入状态下，可以买入，`buy[i]=sell[i-1]-prices[i]`, 也可以啥也不干`buy[i]=buy[i-1]`；同理，在卖出状态下，`sell[i]=buy[i-1]+prices[i]-fee Or sell[i]=sell[i-1]`，两种选项中取最大的就好了。

**初始状态** `buy[0]=-prices[0], sell[0]=0`，最后只要返回在最后一天的卖出状态的收益

```Java
class Solution {
    public int maxProfit(int[] prices, int fee) {
        if(prices.length<=1)  return 0;
        int[] buy=new int[prices.length];
        int[] sell=new int[prices.length];
        buy[0]=-prices[0];
        sell[0]=0;
        for(int i=1; i<prices.length; i++){
            buy[i]=Math.max(buy[i-1], sell[i-1]-prices[i]);
            sell[i]=Math.max(sell[i-1], buy[i-1]+prices[i]-fee);
        }
        return sell[prices.length-1];
    }
}
```

此时时间复杂度 O(n),空间复杂度 O(n)。因为我们发现最新的状态只与上一次状态有关，那么保存这么多状态就没有意义，就可以将空间复杂度降为常数

```Java
class Solution {
    public int maxProfit(int[] prices, int fee) {
        if(prices.length<=1)    return 0;
        int buy=-prices[0];
        int sell=0;
        for(int i=1; i<prices.length; ++i){
            buy=Math.max(buy, sell-prices[i]);
            sell=Math.max(sell, buy+prices[i]-fee);
        }
        return sell;
    }
}
```

## [123 Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/)

> Say you have an array for which the ith element is the price of a given stock on day i.

> Design an algorithm to find the maximum profit. You may complete at most two transactions.

1. 定义状态
   `f(k,i)`表示 the profit at most k transactions at ith day
2. 状态转移方程
   `f(k,i)=max(f(k,i-1), f(k-1,j)+prices[i]-prices[j]), j<i and make the expression max`
   `f(k,i)=max(f(k,i-1), prices[i]+max(f(k-1,j)-prices[j])`
3. 初始状态
   `f(k,0)=0;  f(0,i)=0`

有了这些条件就好做了
```Java
class Solution {
    public int maxProfit(int[] prices) {
        if(prices.length<=1)    return 0;
        int[][] dp=new int[3][prices.length];
        int ans=Integer.MIN_VALUE;
        for(int k=1; k<3; ++k){
            int lastProfit=dp[k-1][0]-prices[0];
            for(int i=1; i<prices.length; ++i){
                dp[k][i]=Math.max(dp[k][i-1], prices[i]+lastProfit);
                lastProfit=Math.max(lastProfit, dp[k-1][i]-prices[i]);
            }
        }
        return dp[2][prices.length-1];
    }
```
时间复杂度和空间复杂度都为 O(kn)，还有更简单的方法，只维持一时的状态，很难表达清楚， 看代码吧

```Java
class Solution {
    public int maxProfit(int[] prices) {
        if(prices.length<=1)    return 0;
        int firstBuy=Integer.MIN_VALUE;
        int secondBuy=Integer.MIN_VALUE;
        int firstSell=0;
        int secondSell=0;
        for(int i=0; i<prices.length;++i){
            int p=prices[i];
            secondSell=Math.max(secondSell, p+secondBuy);
            secondBuy=Math.max(secondBuy, firstSell-p);
            firstSell=Math.max(firstSell, p+firstBuy);
            firstBuy=Math.max(firstBuy, -p);           
        }
        return secondSell;
    }
}
```
时间复杂度为 O(n), 空间复杂度为 O(1)

## [518 Coin Change 2](https://leetcode.com/problems/coin-change-2/)

> You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

定义状态：`dp[i][j]` 表示用了前 i 个 coins 到达 amount j 的组合数（这都咋想出来的啊）

初始：`dp[0][0]=1`

`dp[i][j]=dp[i-1][j]+dp[i][j-coins[i]]`

```Java
class Solution {
    public int change(int amount, int[] coins) {
        int[][] dp=new int[coins.length+1][amount+1];
        dp[0][0]=1;
        for(int i=1; i<coins.length+1; ++i){
            for(int j=0; j<amount+1; ++j){
                dp[i][j]=dp[i-1][j]+ (j>=coins[i-1]?dp[i][j-coins[i-1]]:0);
            }
        }
        return dp[coins.length][amount];
    }
}
```

此时注意到`dp[i][j]`只跟上一行的`dp[i-1][j]`有关系，意味着可以缩短空间复杂度

```Java
class Solution {
    public int change(int amount, int[] coins) {
        int[] dp=new int[amount+1];
        dp[0]=1;
        for(int coin:coins){
            for(int i=coin; i<amount+1; ++i)
                dp[i]+=dp[i-coin];
        }
        return dp[amount];
    }
}
```

## [309 Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)

> Say you have an array for which the ith element is the price of a given stock on day i.

> Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

> - You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
> -After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

The natural states for this problem are `buy` and `sell`

- `buy[i]` means the maxProfit end with buy at day i
- `sell[i]` means the maxProfit end with sell at day i

Then we have the transition function:

- `buy[i]=max(buy[i-1], sell[i-2]-prices[i]) (i>=2) buy[i]=max(buy[i-1], -prices[i] (i<2)`
- `sell[i]=max(sell[i-1], buy[i-1]+prices[i]`

```Java
class Solution {
    public int maxProfit(int[] prices) {
        if(prices.length<=1)    return 0;
        int[] buy=new int[prices.length];
        int[] sell=new int[prices.length];
        buy[0]=-prices[0];
        for(int i=1; i<prices.length;++i){
            if(i>1)
                buy[i]=Math.max(buy[i-1], sell[i-2]-prices[i]);
            else
                buy[i]=Math.max(buy[i-1], -prices[i]);
            sell[i]=Math.max(sell[i-1], prices[i]+buy[i-1]);
        }
        return sell[prices.length-1];
    }
}
```

Since the curr state is only related to the 1 step previous state, we can reduce the spacial complexity to O(1).

```Java
class Solution {
    public int maxProfit(int[] prices) {
        if(prices.length<=1)    return 0;
        int buy=-prices[0],preBuy=0;
        int preSell=0, sell=0;
        for(int i=1; i<prices.length; ++i){
            preBuy=buy;
            buy=Math.max(buy, preSell-prices[i]);
            preSell=sell;
            sell=Math.max(sell, prices[i]+preBuy); 
        }
        return sell;
    }
}
```

## [10 Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/)

> Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

> '.' Matches any single character.
> '*' Matches zero or more of the preceding element.
> The matching should cover the entire input string (not partial).

> Note:

> s could be empty and contains only lowercase letters a-z.
> p could be empty and contains only lowercase letters a-z, and characters like . or *.

```
1, If p.charAt(j) == s.charAt(i) :  dp[i][j] = dp[i-1][j-1];
2, If p.charAt(j) == '.' : dp[i][j] = dp[i-1][j-1];
3, If p.charAt(j) == '*': 
   here are two sub conditions:
               1   if p.charAt(j-1) != s.charAt(i) && p.charAt(j-1)!='.' : dp[i][j] = dp[i][j-2]  //in this case, a* only counts as empty
               2   if p.charAt(i-1) == s.charAt(i) or p.charAt(i-1) == '.':
                              dp[i][j] = dp[i-1][j]    //in this case, a* counts as multiple a 
                           or dp[i][j] = dp[i][j-1]   // in this case, a* counts as single a
                           or dp[i][j] = dp[i][j-2]   // in this case, a* counts as empty
```

目前有一点不理解，`p.charAt(j) == '*'  p.charAt(i-1)==s.charAt(i) or p.charAt(i-1) == '.'` 为啥 ` dp[i][j] = dp[i-1][j]` 不是 ` dp[i][j] = dp[i-1][j-1]`

这里还要注意一些 corner case：

```
""
".**********"
```

```Java
class Solution {
    public boolean isMatch(String s, String p) {
        if((s==null && p==null) ||(s.length()==0 && p.length()==0))    return true;
        if(s==null || p==null)    return false;
        int n=s.length();
        int m=p.length();
        boolean[][] dp=new boolean[n+1][m+1];
        dp[0][0]=true;
        for (int i = 0; i < p.length(); i++) {
            if (p.charAt(i) == '*' && dp[0][i-1]) 
                dp[0][i+1] = true;
        }
        for(int i=1; i<n+1; ++i){
            for(int j=1; j<m+1; ++j){
                if(s.charAt(i-1)==p.charAt(j-1) || p.charAt(j-1)=='.')
                    dp[i][j]=dp[i-1][j-1];
                else if(p.charAt(j-1)=='*'){
                    if(j>1 && p.charAt(j-2)!=s.charAt(i-1) && p.charAt(j-2)!='.')
                        dp[i][j]=dp[i][j-2];
                    else if(j>1 && (p.charAt(j-2)==s.charAt(i-1) || p.charAt(j-2)=='.')){
                        dp[i][j]=(dp[i][j-1] || dp[i][j-2] || dp[i-1][j-1] || dp[i-1][j]);
                        
                    }
                }
            }
        }
        return dp[n][m];
    }
}
```