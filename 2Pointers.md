## Sliding Window

**Explain the time complexity** Time Complexity will be O(n) because the "start" and "end" points will only move from left to right once.

**Using a count to flag whether meet the requirement. And if the elements are characters, we can use an array instead of map.**

In any sliding window based problem we have two pointers. 
One rightright pointer whose job is to expand the current window and 
then we have the leftleft pointer whose job is to contract a given window.
At any point in time only one of these pointers move and the other one remains fixed.

对 sliding window 问题，我们用两个指针，右指针用于扩展当前窗口，左指针用于缩小窗口。在任何时间点，只有一个指针移动，而另外一个静止。

### [76 Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)  :triangular_flag_on_post:

> Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

关于 sliding window 这类问题，这个题目的讨论中有答题模板，忘了怎么写可以去看一看，点击题目超链接就可。

对于这个问题，这里用了一个数组作为 dictionary 来查询 T 中元素的个数，比用 hashmap 方便些。另外不需要实时记录 substring，而是记录其起始位置，随后截取 substring。另外用一个 `counter` 来表示此事的 substring 是否是 valid。如果在移动 left 指针时，如果 `A[left]!=0`，就说明这个 char 不在 T 中。

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

### [438 Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)  :triangular_flag_on_post:

> Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

> Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

> The order of output does not matter

```Java
class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> ans=new ArrayList();
        if(s==null || p==null || s.length()<p.length())   return ans;
        int[] dict=new int[256];
        int left=0, right=0, counter=p.length();
        for(int i=0; i<p.length(); ++i){
            dict[p.charAt(i)]++;
        }
        while(right<s.length()){
            char c=s.charAt(right);
            if(dict[c]-->0)
                counter--;
            ++right;
            
            while(counter==0){
                char c2=s.charAt(left);
                if(right-left==p.length())
                    ans.add(left);
                if(dict[c2]++>=0)
                    counter++;
                left++;
            }
        }
        return ans;
    }
}
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

## General

### [986 Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/) :triangular_flag_on_post:

> Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

> Return the intersection of these two interval lists.

两个指针，一个指一个 list，然后谁的屁股考前移动谁。这里题可以注意一下 Java 的写法。

```Java
class Solution{
    public int[][] intervalIntersection(int[][] A, int[][] B){
        List<int[]> ans=new ArrayList();
        int i=0, j=0;
        while(i<A.length && j<B.legnth){
            int start=Math.max(A[i][0], B[j][0]);
            int end=Math.min(A[i][1], B[j][1]);
            if(start<=end)  
                ans.add(new int[]{start, end});// 类似于 C++也可以用初始化列表
            if(A[i][1]>B[j][1])
                ++j;
            else
                ++i;
        }
        int[][] res=new int[ans.size()][2];
        i=0;
        for(int[] pair: ans){   // List 可以这样遍历
            res[i++]=pair;
        }
        return res;
    }
}
```

### [3 Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/solution/)

> Given a string, find the length of the longest substring without repeating characters.

跟上面的题目一样，他们写 sliding window 两个指针一块放到 while 条件语句里。而不是像我自己想的那样嵌套两个 while

```Java
public class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length();
        Set<Character> set = new HashSet<>();
        int ans = 0, i = 0, j = 0;
        while (i < n && j < n) {
            // try to extend the range [i, j]
            if (!set.contains(s.charAt(j))){
                set.add(s.charAt(j++));
                ans = Math.max(ans, j - i);
            }
            else {
                set.remove(s.charAt(i++));
            }
        }
        return ans;
    }
}
```

当然这个题也可以用 map 来放索引值，这样一次性调到下一个不重复的位置。

```Java
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n=s.length();
        int ans=0;
        int left=0,right=0;
        Map<Character, Integer> dict=new HashMap();
        for(;right<n; ++right){
            if(dict.containsKey(s.charAt(right)))
                left=Math.max(left,dict.get(s.charAt(right)));
            ans=Math.max(ans, right-left+1);
            dict.put(s.charAt(right), right+1);
        }
        return ans;
    }
}
```