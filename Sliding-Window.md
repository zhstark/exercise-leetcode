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