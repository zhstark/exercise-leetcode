In any sliding window based problem we have two pointers. 
One rightright pointer whose job is to expand the current window and 
then we have the leftleft pointer whose job is to contract a given window.
At any point in time only one of these pointers move and the other one remains fixed.

对 sliding window 问题，我们用两个指针，右指针用于扩展当前窗口，左指针用于缩小窗口。在任何时间点，只有一个指针移动，而另外一个静止。

### Problem 76 Minimum Window Substring

用 counter 结合Counter(substring) 来记录判断是否已包换全部 substring
比较 subtring 长度后记得更新 substring 长度（length）

```py
class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        T = collections.Counter(t)
        counter = len(t)
        left = 0
        right = 0
        length = float("inf")
        ans = ""
        while right < len(s):
            if s[right] in T:
                T[s[right]] -= 1
                if T[s[right]] >= 0:
                    counter -= 1
            while counter == 0:
                if right-left+1 < length:
                    length = right-left+1
                    ans = s[left:right+1]
                if s[left] in T:
                    T[s[left]] += 1
                    if T[s[left]] > 0:
                        counter += 1

                left += 1
            right += 1

        return ans
```

### Problem 995. Minimum Number of K Consecutive Bit Flips

假设用 flippedTime 来表示 A[i] 被之前元素翻转所影响的次数， 那么如果 flippedTime 是偶数且 A[i]=0, 或者 flippedTime 是奇数且 A[i]=1，那么 A[i] 就需要被翻转。
用代码表示为如果 flippedTime%2==A[i]，那么 A[i] 需要被翻转。

因为我们每次都要对长度为 K 的区间进行翻转，假设存在一个 window 在闭区间 [i-K, i-1]，当 i<K 时，即为 [0, K-1]。用 flippedTime 计算在该 window 里发生翻转的次数。

当 i>=K 时，对 A[i] 是否翻转产生影响的应该是在区间 [i-K+1, i-1]内的。所以我们检测 A[i-k]是否发生翻转，如果 A[i-K] 翻转了，那么就把 flippedTime-1，此时 flippedTime 即为 A[i]在此之前被翻转的次数。这时再判断 A[i] 是否要被翻转。

在代码中，如果 A[j] 被翻转了，就把其值设为2，便于之后的检测。

```py
class Solution:
    def minKBitFlips(self, A: 'List[int]', K: 'int') -> 'int':
        flippedTime=0
        count=0
        for i in range(len(A)):
            if i>=K and A[i-K]==2:
                flippedTime-=1
                
            if (flippedTime %2) == A[i]:
                if i+K>len(A):
                    return -1
                A[i]=2
                flippedTime+=1
                count+=1
                
        return count
```