## 493 Reverse Pairs

[link](https://leetcode.com/problems/reverse-pairs/)

Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.

Basic idea is backtracking to compare all the combinations. The time complexity is O(n^2), not good enough.

We know that we need to compare 2 elememts in order to check if it is a Revers pair, which is similar to sort.

In merge sort, before we merge two subarrays, we have two sorted subarrays. We can count reverse pairs in this stage. Since the subarray is sorted, we have no need to compare all the combinations. If A_x > 2*B_y, then A_x is bigger than all the elements before y in subarray B.

Assuming we have 2 2-elements subarrays, we use 2 pointers p and q pointing to the last elements in the subarrays.

_ _    _ _

  p      q

If p\>2\*q, then p must \>2\*(q-1). So count+=q-left2+1.

If p<=2\*q, then we move q backword, and compare again.

```cpp
class Solution {
public:
    int reversePairs(vector<int>& nums) {
        int n=nums.size();
        if(n==0)    return 0;
        int count=0;
        merge_sort(nums, count);
        return count;
    }
private:
    void merge(vector<int>& nums, int left1, int right1, int left2, int right2){
        int i=left1, j=left2;
        int x[right2-left1+1];
        int n=0;
        while(i<=right1 && j<=right2){
            nums[i]<=nums[j] ? x[n++]=nums[i++] : x[n++]=nums[j++];
        }
        while(i<=right1){
            x[n++]=nums[i++];
        }
        while(j<=right2){
            x[n++]=nums[j++];
        }
        for(i=0;i<right2-left1+1;++i){
            nums[i+left1]=x[i];
        }
    }
    int merge_sort_rec(vector<int>& nums, int left, int right){
        if(left>=right) return 0;
        int mid=(left+right)/2;
        int count=merge_sort_rec(nums, left, mid)+merge_sort_rec(nums, mid+1, right);
        int p1=mid, p2=right;
        while(p1>=left && p2>=mid+1){
            if(nums[p1]> 2LL * nums[p2]){
                count+=p2-mid;
                --p1;
            }
            else{
                --p2;
            }
        }
        merge(nums, left, mid, mid+1, right);
        return count;
    }
    
    void merge_sort(vector<int>& nums, int& count){
        count=merge_sort_rec(nums, 0, nums.size()-1);
    }
};
```