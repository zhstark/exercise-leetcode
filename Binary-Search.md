## 注意事项：

1. **在`while`循环里面，`l<=r`**
2. mid 取值：`mid=l+(r-l)//1` (python)
3. 更新的时候， **l=mid+1, not l=mid**，r 同理
4. 先检测是否不满足条件，在检测是否满足条件
5. ">>"的优先级低于"+"，所以除以二的时候用位移记得加括号

## 花式二分法

### 查找第一个 值 等于给定值的元素

```py
def BS_1(array, value):
    l,r=0,len(array)-1
    while l<=r:
        mid=l+(r-l)>>1
        if array[mid]>value:
            r=mid-1
        elif array[mid]<value:
            l=mid+1
        else:
            if mid==0 or array[mid-1]!=value:
                return mid
            else:
                r=mid-1
    
    return -1
```

### 查找最后一个值等于给定值的元素

```py
def BS_2(array, value):
    l,r=0,len(array)-1
    while l<=r:
        mid=l+(r-l)>>1
        if array[mid]>value:
            r=mid-1
        elif array[mid]<value:
            l=mid+1
        else:
            if mid==len(array)-1 or array[mid+1]!=value:
                return mid
            else:
                l=mid+1
    
    return -1
```

### 查找第一个大于等于给定值的元素 (>=value)

```py
def BS_3(array, value):
    l,r=0,len(array)-1
    while l<=r:
        mid=l+((r-l)>>1)
        if array[mid]>=value:
            if mid==0 or array[mid-1]<value:
                return mid
            else:
                r=mid-1
        else:
            l=mid+1
    return -1
```

### 查找最后一个小于或等于给定值得元素 (<=value)

```py
def BS_4(array, value):
    l,r=0,len(array)-1
    while l<=r:
        mid=l+(r-l)>>1
        if array[mid]<=value:
            if mid==len(array)-1 or array[mid+1]>value:
                return mid
            else:
                l=mid+1
        else:
            r=mid-1
    return -1

```

## 后记

数据量太大不太适合二分查找，因为二分法依赖数组，而数组是内存连续空间

## [154 Find Minimum in Rotated Sorted Array II](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/)

> Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
> (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
> Find the minimum element.
> The array may contain duplicates.

Since the array is sorted anyway, we will consider binary search method to solve it.

When updating `left` and `right`, since we mean to find the minimum, when mid<right, we do not know if mid is the minimum or not, so we update `right` to be mid not mid-1.

When we meet duplicate number (`A[mid]==A[right]`), binary search is not useful, turn to using linear search until we meet different numbers.

```cpp

class Solution {
public:
    int findMin(vector<int>& nums) {
        if(nums.size()==0)  return -1;
        int left=0;
        int right=nums.size()-1;
        while(left<right){
            int mid=left+(right-left)/2;
            if(nums[mid]>nums[right])   left=mid+1;
            else if(nums[mid]<nums[right]) right=mid;
            else    --right;
        }
        return nums[left];
    }
};
```

## [81 Search in Rotated Sorted Array II](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/)

> Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
> (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
> You are given a target value to search. If found in the array return true, otherwise return false.> 

The key of binary search is the body in the while loop.

Firsty check return condition.

Then if we meet duplicate numbers, move one step.

Then like normal binary search.

```cpp

class Solution {
public:
    bool search(vector<int>& nums, int target) {
        if(nums.size()==0)  return false;
        int left=0, right=nums.size()-1;
        while(left<=right){
            int mid=left+(right-left)/2;
            if(nums[mid]==target)   return true;
            if(nums[mid]==nums[right])  --right;
            else if(nums[mid]>nums[right]){
                if(target>=nums[left] && target<nums[mid])
                    right=mid-1;
                else
                    left=mid+1;
            }
            else{
                if(target>nums[mid] && target<=nums[right])
                    left=mid+1;
                else
                    right=mid-1;
            }
        }
        return false;
    }
};

```
