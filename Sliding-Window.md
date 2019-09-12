In any sliding window based problem we have two pointers. 
One rightright pointer whose job is to expand the current window and 
then we have the leftleft pointer whose job is to contract a given window.
At any point in time only one of these pointers move and the other one remains fixed.

对 sliding window 问题，我们用两个指针，右指针用于扩展当前窗口，左指针用于缩小窗口。在任何时间点，只有一个指针移动，而另外一个静止。

## [76 Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)  :triangular_flag_on_post:

> Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

关于 sliding window 这类问题，这个题目的讨论中有答题模板，忘了怎么写可以去看一看，点击题目超链接就可。

对于这个问题，这里用了一个数组作为 dictionary 来查询 T 中元素的个数，比用 hashmap 方便些。另外不需要实时记录 substring，而是记录其起始位置，随后截取 substring。另外用一个 `counter` 来表示此事的 substring 是否是 valid。

Java

```Java
class Solution {
    public String minWindow(String s, String t) {
        int[] dic=new int[128];
        for(int i=0; i<t.length(); ++i){
            dic[t.charAt(i)]++;
        }
        int left=0, right=0;
        int head=0;
        int counter=t.length();
        int length=Integer.MAX_VALUE;//record the length of valid result
        while(right<s.length()){
            if(dic[s.charAt(right)]>0){
                counter--;
            }
            dic[s.charAt(right)]--;
            right++;
            while(counter==0){
                if(length>right-left){
                    head=left;
                    length=right-left;
                }
                if(dic[s.charAt(left)]==0){
                    counter++;
                }
                dic[s.charAt(left)]++;
                left++;
            }
        }
        return length==Integer.MAX_VALUE? "": s.substring(head, head+length);
    }
}
```

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

### Problem 1004

contest的时候咋就没想到用 slide window啊
现在用 C++了
```C++
class Solution {
public:
    int longestOnes(vector<int>& A, int K) 
    {
        int left=0, right=0;
        int ans=0;
        while(right<A.size())
        {
            if(A[right]==1)
                right++;
            else
            {
                if(K>0)
                {
                    K--;
                    right++;
                }
                else
                {
                    while(A[left]==1)
                        left++;
                    left++;
                    K++;
                }
            }
            ans=max(ans,right-left);
        }
        return ans;
    }
};
```