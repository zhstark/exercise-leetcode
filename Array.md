## 287 Find the duplicate number

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

**You must not modify the array (assume the array is read only).**
**You must use only constant, O(1) extra space.**
**Your runtime complexity should be less than O(n2).**

### Solution 1

We can split the figures of 1\~n into 2 parts from the middle m. Part one is 1\~m, part two is m+1\~n. If the numbers of 1\~m is more than m, than this part must has the duplicate number. Then we split this part again, like binary search. So the time complexity is O(nlogn), the sapcial complexity is O(1).

```cpp

class Solution {
public:
	int findDuplicate(const vector<int>& nums) {
		int n=nums.size();
		int left=1;
		int right=n-1;
		while(left<=right){
			int mid=left+((right-left)>>1);
			if(left==right) return left;
			int count=countNum(nums, left, mid);
			if(count<=mid-left+1)   left=mid+1;
			else    right=mid;  
		}
		return -1;
	}
private:
	int countNum(const vector<int>& nums, int left,int right){
		int count=0;
		for(auto i: nums){
			if(i>=left && i<=right)
				++count;
		}
		return count;
	}
};
```
### Solution 2

**Floyd's algorithm**

Consider the array as a Linkedlist, where the index is the value of LinkedList node, the value of the array is the index of the next node.

Let's see an array like this:

| value | 1 | 3 | 4 | 2 | 2 |

| index | 0 | 1 | 2 | 3 | 4 |

Consider the array as a LinkedList: 1->3->2->4->2

Then this problem has been turned into " Whether a LinkedList has a circle and find the entrance if there is a circle." 

Stage 1:

Set 2 pointers *slow* and *fast* point to the first node. Then pointer *slow* move 1 node per step while *fast* move 2 nodes per step. If there is a circle, *slow* will meet *fast* finally.

Stage 2:

Move *fast* back to the first node. And make it move 1 node per step. Now, *slow* and *fast* will meet in the entrance.

The proof:(https://leetcode.com/problems/linked-list-cycle-ii/solution/#approach-2-floyds-tortoise-and-hare-accepted)

and my notes of this proof:

![](IMG_6892FF5D41DA-1.jpeg)

```cpp
class Solution {
public:
    int findDuplicate(const vector<int>& nums) {
        if( nums.size()==0) return -1;
        int slow=nums[0];
        int fast=nums[0];
        slow=nums[slow];
        fast=nums[nums[fast]];
        while(slow!=fast){
            slow=nums[slow];
            fast=nums[nums[fast]];
        }
        fast=nums[0];
        while(fast!=slow){
            fast=nums[fast];
            slow=nums[slow];
        }
        return fast;
    }
};
```

## 240. Search a 2D Matrix II

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

- Integers in each row are sorted in ascending from left to right.
- Integers in each column are sorted in ascending from top to bottom.

Provide an example and analyse it. I find that if I start from the right-top, there is a rule that make this problem very easy.

Start from thr right-top, in the same row, every elements in the left of the number is smaller than it, in the same column, every elements below the number is larger than it. So in each iteration, we can eliminate a row or a column. If the target is larger than it, we know this row can not have the same value, we move the right-top down to next row. If the target is smaller than it, we know this column can not have the same value, we move the right-top left to next column, until we find the value or know there is not such a value. Time complexity is O(m+n), spacial complexity is O(1).

```cpp
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if(matrix.size()==0 || matrix[0].size()==0) return false;
        int n=matrix.size(), m=matrix[0].size();
        int row=0, col=m-1;
        while(row<n && col>=0){
            if(matrix[row][col]==target)    return true;
            if(target<matrix[row][col]) --col;
            else ++row;
        }
        return false;
    }
};
```

## 442. Find All Duplicates in an Array

[link](https://leetcode.com/problems/find-all-duplicates-in-an-array/)

Since 1 ≤ a[i] ≤ n, if there is no duplicate figure, this array can be permutated that for index i, the value is i+1. When there are duplicate figures and we permutate it again, there are some index that we can not find i+1 to match it and there are some value j that can not put to index j-1 again because index j-1 has already had a value j on it. We solve this problem according to this rule.

Traversing the array, when we traverse the index i, we check whether the value m is equal to i+1. If no, we compare this value to the value in index m-1, if these values are same, we find a duplicated number, if not, we swap these value, so we put m in right position: the index m-1 has value m. Then we check index i again and repeat this process.

If a number is duplicated more than twice, the above method will get this number more than one time. In order to avoid duplication, when we find a duplicated number, we set the value to -1 to mark that it has been got before.

```cpp
class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        vector<int> ans;
        //corner case
        int n=nums.size();
        if(n==0) 
            return ans;
        
        for(int i=0;i<n;++i){
            int d=nums[i]-1;
            if(d!=i){
                //got this value before
                if(d==-2 || nums[d]==-1)
                    continue;
                else if(nums[d]==nums[i]){
                    ans.push_back(d+1);
                    nums[d]=-1;
                }
                else{
                    swap(nums[i], nums[d]);
                    --i;
                }
            }
        }
        return ans;
    }
};
```

## [1089 Duplicate Zeros](https://leetcode.com/problems/duplicate-zeros/)

> Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

> Note that elements beyond the length of the original array are not written.

> Do the above modifications to the input array in place, do not return anything from your function.

Assuming that we use extra space to show the result of shifting, firstly we count how many zeros there are, then we set a longer array with size of arr.size()+number_of_zeros, which store the result of shifting. Then we pass backword (from right to left), and move item from old array to new array. When we meet zero, we duplicate it.

```cpp

void duplicateZeros(vector<int>& arr) {
    int zeros=0;
    for(auto a: arr){
        if(a==0)    ++zeros;
    }

    // Set a new array
    vector<int> arr2(arr.size()+zeros);

    // shuffle from old array into new array
    for(int i=arr.size()-1, int j=arr2.size()-1; i>=0 && j>=0; --i, --j){
        if(arr[i]!=0)
            arr2[j]=arr[i];

        // Meet zeor, duplicate it  
        else{
            arr2[j]==arr[i];
            arr2[--j]=arr[i];
        }
    }
    for(int i=0; i<arr.size(); ++i)
        arr[i]=arr2[i];
}
```

However, since `i` is always ahead of `j`, when we change `A[j]`, it will not influence any elements we will pass, so we donot need to set another array, but just manipulate original array.

```cpp

void duplicateZeros(vector<int>& arr) {
    int zeros=0;
    for(auto a: arr){
        if(a==0)    ++zeros;
    }
    
    int n=arr.size();
    
    for(int i=n-1, j=n-1+zeros; i>=0 && j>=0; --i, --j){
        if(arr[i]!=0){
            if(j<n) arr[j]=arr[i];
        }
        else{
            if(j<n) arr[j]=arr[i];
            --j;
            if(j<n) arr[j]=arr[i];
        }
    }
}
```

Java

```Java

class Solution {
    public void duplicateZeros(int[] A) {
        int n = A.length, i = 0, j = 0;
        for (i = 0; i < n; ++i, ++j) {
            if (A[i] == 0) ++j;
        }
        for(i=n-1, j=j-1; j>=0 && i>=0; --i,--j){
            if(A[i]!=0){
                if(j<A.length)
                    A[j]=A[i];
            }
            else{
                if(j<A.length)  A[j]=A[i];
                --j;
                if(j<A.length)  A[j]=A[i];
            }
        }
    }
}
```

## [31 Next Permutation](https://leetcode.com/problems/next-permutation/)  :triangular_flag_on_post:

> mplement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

> If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

> The replacement must be in-place and use only constant extra memory.

The point is how to find the regularity. Let's see some examples:
```
1 2 3 4 5
1 2 3 5 4   <---
1 2 4 3 5   <---
1 2 4 5 3
1 2 5 3 4
1 2 5 4 3   <----
1 3 2 4 5   <----
```
See the pointed part. we could notice that if from `a[i]`, the right part of `a[i] (a[i+1],a[i+2]...)` is decending, we need to put another number into this part, which also mean we gotta move a number out of it. So which number would be? If we want to have the next permutation, the number that move out from decending part must be the minimum number that is bigger than the new inserted number. After changing the number, reverse the decending part. Than get the answer. However, what if the whole array is decending at the first place? Check it. when we find the index of the decending begining, if it is 0, just reverse the array and return.

此题难点在于理清逻辑，找个下个组合与当前组合的关系：需要如何排列

1. 找到相邻的两个点，`a[i], a[i-1]`，满足`a[i]>a[i-1]`，并且自`a[i]`往后为递减。（倒着找方便）
2. 在`a[i]` 开始递减的部分中找到比`a[i-1]`大的最小的数，设为`a[j]`，那么`a[j]` 应该换在 `a[i-1]` 的位置。（倒着找）
3. 将`i-1`后的数升序排列，因为将`a[i-1], a[j]` 互换后，这些数仍是降序，所以只要将其翻转就好了

时间复杂度 O(3*n)

```Java
class Solution {
    public void nextPermutation(int[] nums) {
        if(nums.length<=1)  return;
        int i=nums.length-1;
        for(;i>0; --i){
            if(nums[i]>nums[i-1])
                break;
        }
        if(i<=0){
            reverse(nums, 0);
            return;
        }
        int j=nums.length-1;
        for(;j>=0; --j){
            if(nums[j]>nums[i-1])
                break;
        }
        swap(nums, i-1, j);
        reverse(nums, i);
    }
    public void swap(int[] nums, int index1, int index2){
        int temp=nums[index1];
        nums[index1]=nums[index2];
        nums[index2]=temp;
    }
    public void reverse(int[] nums, int index){
        int i=index, j=nums.length-1;
        while(i<j){
            swap(nums, i,j);
            ++i;
            --j;
        }
    }
}
```