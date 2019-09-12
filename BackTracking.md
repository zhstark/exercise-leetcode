## [301 Remove Invalid Parentheses](https://leetcode.com/problems/remove-invalid-parentheses/) :triangular_flag_on_post:

> Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

> Note: The input string may contain letters other than the parentheses ( and ).

Since the output are all possible results, we consider bractracking method. 

However, since we only need results that remove the minimum number of invalid parentheses, if we just try all the results, we may get many expression that we don't want. 

So what if we could count the invalid parentheses?

1. We process the expression one bracket at a time starting from the left.
2. Suppose we encounter an opening bracket i.e.`(`, it may or may not lead to an invaild expression because there can be a matching ending bracket somewhere in the remaining part of the expression. Here, we simply increment the counter keeping track of left parantheses till now. `left+=1`
3. If we encounter a closing bracket, this has two meanings:
   - Either there was no matching opening bracket for this closing bracket and in that case we have an invalid expression. This is the case when `left==0` i.e. when there are no unmatched left brackets available. In such a case we increment another counter say `right+=1` to represent misplaced right parentheses.
   - Or ,we had some unmatch opening bracket available to match this closing bracket. This is the case when `left>0`. In this case we simply decrement the left counter.`left-=1`
4. Continue processing the string until all parentheses have been processed.
5. In the end, the `left` will be the number of invalid opening bracket and `right` will be the number of invalid closing bracket.

Then we can use these to do backtracking, which may save a lot of time.

```cpp
class Solution {
public:
    vector<string> removeInvalidParentheses(string& s) {
        //find the number of `(` and `)` that need to be removed
        int left=0, right=0;
        for(auto c:s){
            if(c=='(')
                left++;
            else if(c==')'){
                if(left>0)  left--;
                else    right++;
            }
        }
        unordered_set<string> ans;
        string temp="";
        bracktrack(ans,s,0,temp, 0,left, right);
        return vector<string>(ans.begin(),ans.end());

    }
private:
    void backtrack(vector<string>& ans, string&s, int idx, string& temp, int left, int right){
        if(left<0 || right<0 || count<0)   return;
        if(idx==s.size()){
            if(left==0 && right==0 && count==0){
                ans.insert(temp);
             }
            return;
        }
        if(s[idx]=='('){
            temp+=s[idx];
            bracktrace2(ans, s, idx+1, temp,count+1, left, right);
            temp.erase(temp.size()-1);
            bracktrace2(ans, s, idx+1, temp,count, left-1, right);
        }
        else if(s[idx]==')'){
            temp+=s[idx];
            bracktrace2(ans,s,idx+1, temp, count-1,left, right);
            temp.erase(temp.size()-1);
            bracktrace2(ans,s,idx+1, temp,count, left,right-1);
        }
        else{
            temp+=s[idx];
            bracktrace2(ans, s, idx+1, temp,count, left, right);
            temp.erase(temp.size()-1);
        }
        return;
    }
};
```



## 282 Expression Add Operators  :triangular_flag_on_post: 

**step1**

- 对输入的数字有不同的切分方式，所以要想办法遍历所有可能的组合。
- 类似有分治排序的分割方法，不同是每次分割都会去组合一遍，而不是把全部分割为单个数字后再组合
- 分割过程还要注意“00”的存在

**step2**
- 遍历所有+ - * 运算。
- 对于‘*’， 需要保存前面挨着的乘法得到的数（没有乘法运算就是上一个数）
- A+B*C 为上一步的表达式，值为curr， 这一步 *d
- 在上一步要保存 prev=B*C 传递到下一次迭代。
- A+B\*C\*d=(A+B\*C)-prev+prev\*d
- 更新 prev=prev*d

C++注意两点：
1. 字符串可能太长，不能用 `stoi`，用`stol`，转换为 long 型
2. 注意 `00`  情况的出现，在主 function 和辅助 function 中都要检查

Python

```python
class Solution:
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        if not num:
            return []
        self.target = target
        l = []

        for i in range(1, len(num)+1):
            if i == 1 or (i > 1 and num[0] != '0'):
                self.helper(int(num[:i]), int(num[:i]), num[i:],  num[:i], l)

        return l

    def helper(self, pre, curr, num, ans, l):
            if not num:
                if curr == self.target:
                    l.append(ans)
                return

            for i in range(1, len(num)+1):
                if i == 1 or (i > 1 and num[0] != '0'):
                    temp = num[:i]
                    # +
                    self.helper(int(temp), curr+int(temp),
                                num[i:], ans+'+'+temp, l)
                    # -
                    self.helper(-int(temp), curr-int(temp),
                                num[i:], ans+'-'+temp, l)
                    # *
                    self.helper(pre*int(temp), curr-pre+pre *
                                int(temp), num[i:],  ans+'*'+temp, l)
```

C++
```cpp
class Solution {
public:
    //1. string to long
    vector<string> addOperators(string num, int target) {
        vector<string> ans;
        if(num.size()==0)
            return ans;
        for(int i=0; i<num.size(); i++){
            if(num[0]=='0' && i>0)
                break;
            long number=stol(num.substr(0,i+1));
            backtracing(num, i+1, target, number, number, num.substr(0,i+1), ans);
        }
        return ans;
    }
    
private:
    void backtracing(string& num, int index, int target, long long curr, long long prev, string temp, vector<string>& ans){
        if(index==num.size()){
            if(curr==target){
                ans.push_back(temp);
            }
            return;
        }
        for(int i=index; i<num.size(); ++i){
            if(num[index]=='0' && i>index)
                break;
            long number=stol(num.substr(index, i-index+1));
            //+
            backtracing(num, i+1, target, curr+number, number, temp+"+"+num.substr(index, i-index+1), ans);
            //-
            backtracing(num, i+1, target, curr-number, -1*number, temp+"-"+num.substr(index, i-index+1), ans);
            //*
            backtracing(num, i+1, target, curr-prev+prev*number, prev*number, temp+"*"+num.substr(index, i-index+1), ans);
        }
        
    }
};
```

Java

```Java
class Solution {
    public List<String> addOperators(String num, int target) {
        List<String> res=new ArrayList();
        if(num==null || num.length()==0)  return res;
        for(int i=0; i<num.length(); ++i){
            if(num.charAt(0)=='0' && i>0)   break;
            String curr=num.substring(0, i+1);
            Long element=Long.parseLong(curr);
            backtracking(num, i+1, target, element, element, curr, res);
        }
        return res;
    }
    
    public void backtracking(String num, int index, int target, Long sum, Long prev, String temp, List<String> res){
        if(index==num.length() && sum==target){
            res.add(temp);
            return;
        }
        
        for(int i=index; i<num.length(); ++i){
            if(num.charAt(index)=='0' && i>index)
                break;
            String curr=num.substring(index, i+1);
            Long element=Long.parseLong(curr);
            //+
            backtracking(num, i+1, target, sum+element, element, temp+"+"+curr, res);
            //-
            backtracking(num, i+1, target, sum-element, -1*element, temp+"-"+curr, res);
            //*
            backtracking(num, i+1, target, sum-prev+prev*element, prev*element, temp+"*"+curr, res);        
        }
    }
}
```

## Problem 39 Combination Sum

犯了2个错误：
1.
最开始传数组：
temp.append(candidates[i])
self.f(candidates[i:], target-candidates[i], l, temp)
这种情况会对上一个 f(x,xx,xxxx)中的 temp 造成影响。所以传数组注意不要对上一个迭代结果产生影响
2.
想象每次迭代的 i：
1-2-1 与 1-1-2重复了，所以要注意不要重复

```python
class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []

        l = []
        candidates.sort()
        temp = []

        self.f(candidates, target, l, temp)
        return l

    def f(self, candidates, target, l, temp):
        for i in range(len(candidates)):
            if candidates[i] > target:
                temp = []
                break
            elif candidates[i] == target:
                l.append(temp+[candidates[i]])
                break
            else:
                self.f(candidates[i:], target-candidates[i],
                       l, temp+[candidates[i]])
```

## Problem 46 Permutations

f(nums) 是传该数组，在原数组上更改
f(nums[:]) 是传数据，原数组不变
我做这个题的方法排名倒数，discuss 有很多其他方法，现在还不能理解
其他 backtrack 的题：78，90，47，39，40，131

```python
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        ans = []
        visited = set()

        self.backtrack(ans, [], nums, visited)
        return ans

    def backtrack(self, l, temp, nums, visited):
        if len(temp) == len(nums):
            l.append(temp)
            return

        for i in range(len(nums)):
            if nums[i] not in visited:
                self.backtrack(l, temp+[nums[i]], nums,
                               visited.union(set([nums[i]])))
```

## Problem 47 Permutations II

方法比上一个优化了一些
这个问题里有重复的数，要想如何才能去掉重复的过程
其实第 i 次 backtrack 就是给数组的第 i 个空填数。
所以思路是如果我这次填了 A，下次还是 A， 那么下次再填 A 的时候我就应该跳过。
但这种方法实现起来总是有 bug，（这个理论的缺陷是：如果这次是 A， 那么下次 A 只有在这个 A 没有用过的时候才能用）
所以转换思路，如果这次该填 A，而且下次还是该填 A，那么我就跳过这次的递归，直接进入下次好了

```py
class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []

        nums.sort()
        ans = []
        self.backtrack(nums, ans, [])
        return ans

    def backtrack(self, nums, ans, temp):
        if len(nums) == 0:
            ans.append(temp[:])
            return

        for i in range(len(nums)):
            if i+1 < len(nums) and nums[i] == nums[i+1]:
                continue
            self.backtrack(nums[:i]+nums[i+1:], ans, temp+[nums[i]])
```

## Problem 40 Combination Sum II

假设我们 temp 为四个 "_ _ _ _"
现在是 "A _ _ _"
下一次填 B： "A B _ _"
等回溯结束，又该填第二个位置时，我们怎么知道这次填的是该位置的第二次或第三次:
在那个 for loop 里， i>0

```py
class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return [[]]

        candidates.sort()
        ans = []
        self.backtrack(candidates, target, ans, [])
        return ans

    def backtrack(self, ca, target, ans, temp):
        if target == 0:
            ans.append(temp)
            return
        if target < 0:
            return
        for i in range(len(ca)):
            if i > 0 and ca[i] == ca[i-1]:
                continue
            self.backtrack(ca[i+1:], target-ca[i], ans, temp+[ca[i]])
```


## 对一个 list 的不同修改的递归方法
比如对`l[x]`，第一次回溯回来改值为1，第二次为2，不需要复制一个数组，改数，传递，只需在传递前在原数组更改，回溯后再改回来

```py
grid[nx][ny] = 3
dfs(step + 1, nx, ny)                    
grid[nx][ny] = 0
```
## 301 Remove Invalid Parentheses

[link](https://leetcode.com/problems/remove-invalid-parentheses/)

Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Since it need to return **all** results, generally we need to use backtracking to try all resultes.

In order to reduce the layers of backtracking, firstly we count how many `(` and how many `)` needs to be removed.

Then recusively backtracking, in the meanwhile, use a variable `pair` to check if the expression is valid or not. When we add a `(` into expression, pair+1, when we add a `)` into expression, pair-1(under the condition pair>1)

```cpp
class Solution {
public:
    vector<string> removeInvalidParentheses(string s) {
        int left_to_move=0, right_to_move=0;
        // count how many ( and ) should be removed in order to make it valid.
        for(auto &c:s){
            if(c==')'){
                if(left_to_move==0) ++right_to_move;
                else    --left_to_move;
            }
            else if(c=='('){
                ++left_to_move;
            }
        }
        unordered_set<string> ans;
        helper(s, 0,left_to_move, right_to_move, 0, "", ans);
        vector<string> res(ans.begin(),ans.end());
        return res;
    }
private:
    void helper(string &s, int index, int left_move, int right_move, int pair, string path, unordered_set<string>& ans){
        if(index==s.size()){
            if(left_move==0 && right_move==0 && pair==0)    ans.insert(path);
            return;
        }
        if(s[index]!='(' && s[index]!=')'){
            helper(s, index+1, left_move, right_move, pair, path+s[index], ans);
        }
        // if (,check if still need to remove it, backtrack remove it and no-remove it
        else if(s[index]=='('){
            //remove it
            if(left_move>0) helper(s, index+1, left_move-1, right_move, pair, path, ans);
            //not remove it
            helper(s, index+1, left_move, right_move, pair+1, path+s[index], ans);
        }
        else{
            if(right_move>0)    helper(s, index+1, left_move, right_move-1, pair, path, ans);
            if(pair>0)  helper(s, index+1, left_move, right_move, pair-1, path+s[index], ans);
        }
    }
};

```