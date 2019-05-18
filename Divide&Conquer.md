## 493 Reverse Pairs

[link](https://leetcode.com/problems/reverse-pairs/)

> Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

> You need to return the number of important reverse pairs in the given array.

Basic idea is using 2 for-loop traversing to compare all the combinations. The time complexity is O(n^2), not good enough.

We know that we need to compare 2 elememts in order to check if it is a Revers pair, which is similar to sort.

In merge sort, before we merge two subarrays, we have two sorted subarrays. We can count reverse pairs in this stage. Since the subarray is sorted, we have no need to compare all the combinations. If A_x > 2*B_y, then A_x is bigger than all the elements before y in subarray B.

Assuming we have 2 2-elements subarrays, we use 2 pointers p and q pointing to the last elements in the subarrays.

_ _   \ _ _

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

## 315 Count of Smaller Numbers After Self

[link](https://leetcode.com/problems/count-of-smaller-numbers-after-self/)

> You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Very similar to the above question. The trick is use a vector `index` to map the indices of merged array to the indices of origin array.

And for shuffling the elements in `merge`, we can use std::move.

```cpp
class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        int n=nums.size();
        vector<int> count(n,0);
        vector<int> index(n);
        iota(index.begin(), index.end(),0);
        merge_sort(nums, count, index);
       
        return count;
    }
private:
    void merge_sort(vector<int>& nums, vector<int>& count, vector<int>& index){
        merge_rec(nums, count, index, 0, nums.size()-1);
    }
    void merge_rec(vector<int>& nums, vector<int>& count, vector<int>& index, int left, int right){
        if(left>=right) return;
        int mid=(left+right)/2;
        merge_rec(nums, count, index, left, mid);
        merge_rec(nums, count, index, mid+1, right);
        // counting
        int p=mid, q=right;
        while(p>=left && q>mid){
            int idx1=index[p], idx2=index[q];
            if(nums[idx1]>nums[idx2]){
                count[idx1]+=q-mid;
                --p;
            }
            else{
                --q;
            }
        }
        merge(nums, count, index, left, mid, mid+1, right);
    }
    void merge(vector<int>& nums, vector<int>& count, vector<int>& index, int left1, int right1, int left2, int right2){
        int n=right2-left1+1;
        int x[n];
        n=0;
        int i=left1, j=left2;
        while(i<=right1 && j<=right2){
            int idx1=index[i], idx2=index[j];
            if(nums[idx1]<=nums[idx2]){
                x[n++]=index[i++];
            }
            else{
                x[n++]=index[j++];
            }
        }
        while(i<=right1){
           x[n++]=index[i++];
        }
        while(j<=right2){
           x[n++]=index[j++];
        }
        move(x, x+n, index.begin()+left1);
    }
};
```

## 327 Count of Range Sum

[link](https://leetcode.com/problems/count-of-range-sum/)

> Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
> Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i ≤ j), inclusive.

> Note:
> A naive algorithm of O(n2) is trivial. You MUST do better than that.

In above questions, we compared Reverse Pairs which means `S[j]-S[i]<0 (j>i)`, while in this case, we compare`a<=S[j]-S[i]<=b (j>i)`, where `S[i]` is the sum of first i elements.

Using merge sort again. But in this case, when we count, we use two pointers `p` and `q` begining from the middle. We pass `p` forword if `S[p]<S[i]+a`, pass `q` forword if `S[q]<=S[i]+b`. Then all the element between p and q are the elements that meet the requirement.

Tips:

- Since we calculate the **sum** of the nums, the elements might be very large. So for the array `S`, we set the type of elements be `long long`.
- In this case, I used `std::inplace_merge` to merge, which is much easier.

```cpp
class Solution {
public:
    int countRangeSum(vector<int>& nums, int lower, int upper) {
        if(nums.size()==0)  return 0;
        vector<long long> S(nums.size());
        S[0]=nums[0];
        for(int i=1; i<nums.size();++i){
            S[i]=S[i-1]+nums[i];
        }
        int count=0;
        merge_sort(S, lower, upper, count);
        return count;
    }
private:
    void merge_sort(vector<long long>& S, int lower, int upper, int& count){
        merge_rec(S, lower, upper, count, 0, S.size()-1);
    }
    
    void merge_rec(vector<long long>& S, int lower, int upper, int& count, int left, int right){
        if(left>=right){
            if(S[left]>=lower&&S[left]<=upper)  ++count;
            return;
        }
        int mid=left+(right-left)/2;
        merge_rec(S, lower, upper, count, left, mid);
        merge_rec(S, lower, upper, count, mid+1, right);
        int p=mid+1,q=mid+1;
        for(int i=left; i<mid+1; ++i){
            while(q<=right && S[q]<lower+S[i]) ++q;
            while(p<=right&& S[p]<=upper+S[i]) ++p;
            count+=p-q;
        }
        inplace_merge(S.begin()+left, S.begin()+mid+1,S.begin()+right+1);
    }
};
```