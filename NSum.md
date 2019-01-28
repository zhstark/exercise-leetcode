## 唯一解的 2sum

数组映射到字典：
创建一个 hashtable，对一个 list（array），将数（number） 放到字典的键（key），将索引值（index）放为字典改建的值（value）。

这样遍历数组，如果 target-i 在 hashtable 里，就找到啦，完事。

因为 hashtable 的搜索时间为O(1)，所以时间开销为O(2n)

## 普通2sum

要求列出所有 满足2sum 的值或其值的索引。若是值则不能有重复，比如有了（2，2）就不能再有（2，2），虽然其可能是来自不同位置的 2

先排序，然后两个指针，一个从数组的左端开始，一个从数组的右端开始，然后往中间找。这里有个防重操作，即找到一个后，没有简单的 `l+=1,r-=1`，而是通过两个 `while`跳过重复部分。

```py
# N sum 的子函数， 这里 nums 已经排序好。
def twoSum(self, nums, l, temp, target):
    if len(nums)<2:
        return
    
    left, right=0, len(nums)-1
    while left<right:
        if nums[left]+nums[right]==target:
            l.append(temp+[nums[left],nums[right]])
            left+=1
            right-=1
            while left<right and nums[left]==nums[left-1]:
                left+=1
            while left<right and nums[right]==nums[right+1]:
                right-=1
                
        elif nums[left]+nums[right]>target:
            right-=1
        else:
            left+=1
```

## N sum

用递归遍历所有组合，将 N 降至 2 后转为普通 2sum 问题。

这里在外围递归的时候有个防重，如果这次跟上次相同的位置放的数一样，就跳过

```py
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        
        ans=[]
        def backtrack(nums, temp,N,subtarget):
            if len(nums)<2:
                return
            if N==2:
                l,r=0,len(nums)-1
                while l<r:
                    s=nums[r]+nums[l]
                    if s==subtarget:
                        ans.append(temp+[nums[l],nums[r]])
                        l+=1
                        r-=1
                        while l<r and nums[l]==nums[l-1]:
                            l+=1
                        while r>l and nums[r]==nums[r+1]:
                            r-=1
                            
                        
                    elif s>subtarget:
                        r-=1
                    else:
                        l+=1
                return
       
            for i in range(len(nums)):
                if i>0 and nums[i]==nums[i-1]:
                    continue
                backtrack(nums[i+1:], temp+[nums[i]],N-1, subtarget-nums[i])
        
        nums.sort()        
        backtrack(nums, [],4,target)
        return ans
```