几个基本排序算法代码

- Quick sort
- Merge Sort
- bubbling sort
- Dutch National Flag Problem (75)

## Quick sort

时间复杂度 averge O(nlogn), worst O(n^2). Spacial complexity average O(logn), worst O(n)

```cpp
#include <iostream>
#include <vector>
using namespace std;

int Partition(int v[], int left, int right){
    int p=left;
    int pivot=v[right];
    for(int now=left; now<right; ++now){
        if(v[now]<pivot){
            swap(v[now],v[p]);
            ++p;
        }
    }
    swap(v[p],v[right]);
    return p;
}

void quickSortRec(int v[], int left, int right){
    if(left<right){
        int p=Partition(v, left, right);
        quickSortRec(v, left, p-1);
        quickSortRec(v, p+1, right);
    }
}
void quickSort(int v[], int len){
    quickSortRec(v, 0, len-1);
}

int Partition(vector<int>& arr, int left, int right){
    int p=left;
    int pivot=right;
    for(int now=left; now<right; ++now){
        if(arr[now]<arr[pivot]){
            swap(arr[now], arr[p]);
            ++p;
        }
    }
    swap(arr[p],arr[right]);
    return p;
}

void quickSortRec(vector<int>& arr, int left, int right){
    if(left<right){
        int p=Partition(arr, left, right);
        quickSortRec(arr, left, p-1);
        quickSortRec(arr, p+1,right);
    }
}

void quickSort(vector<int>& arr){
    quickSortRec(arr, 0, arr.size()-1);
}
```

## Merge Sort

```cpp
#include <iostream>
#include <cstdlib>

void Merge(int v[], int left1, int right1, int left2, int right2)
{
    int n = 0;
    int x[right2 - left1 + 1];
    int i = left1, j = left2;
    while (i <= right1 && j <= right2){
        if (v[i] <= v[j])
            x[n++] = v[i++];
        else
            x[n++] = v[j++];
    }
    while (i <= right1){
        x[n++] = v[i++];
    }
    while (j <= right2){
        x[n++] = v[j++];
    }
    for (i = 0; i < right2 - left1 + 1; ++i){
        v[left1 + i] = x[i];
    }
}

void MergeSortRec(int v[], int left, int right)
{
    if (left < right)
    {
        int q = (left + right) / 2;
        MergeSortRec(v, left, q);
        MergeSortRec(v, q + 1, right);
        Merge(v, left, q, q + 1, right);
    }
}
void MergeSort(int v[], int len)
{
    MergeSortRec(v, 0, len - 1);
}

void MergeSortRec(vector<int>::iterator begin, vector<int>::iterator end){
    if(end-begin<=1)   return;
    auto mid=begin+(end-begin)/2;
    MergeSortRec(begin, mid);
    MergeSortRec(mid, end);
    inplace_merge(begin, mid, end);
}
void MergeSort(vector<int>& nums){
    MergeSortRec(nums.begin(), nums.end());
}
```

## bubbling sort

```cpp
#include <iostream>
using namespace std;

int main()
{
    string s1;
    while (cin >> s1)
    {
        int n = s1.size();
        int count = 0;
        int p = 0;
        while (count < n)
        {
            if (isupper(s1[p]))
            {
                char temp = s1[p];
                for (int i = p + 1; i < n; i++)
                {
                    s1[i - 1] = s1[i];
                }
                s1[n - 1] = temp;
            }
            else
                p++;
            count++;
        }
        cout << s1 << endl;
    }

    return 0;
}
```

## [75 Sort Colors](https://leetcode.com/problems/sort-colors/)

> Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

> Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

> Could you come up with a one-pass algorithm using only constant space?

Let's use three to deal with this problem. We use p0 to be the rightmost pointer of 0, p2 to be the leftmost pointer of 2, and curr to be the pointer traversing the array, which means `nums[index<p0]=0` and `nums[index>p2]=2`

So while curr<=p2:
- `if(nums[curr])==0: swap p0 and curr, move p0 and curr forward`
- `if(nums[curr])==1: just move curr forward`
- `if(nums[curr])==2: swap curr and p2, move curr right and p2 left.`

```Java
class Solution {
    public void sortColors(int[] nums) {
        int p0=0,p2=nums.length-1;
        int curr=0;
        while(curr<=p2){
            if(nums[curr]==0){
                swap(nums,curr, p0);
                p0++;
                ++curr;
            }
            else if(nums[curr]==2){
                swap(nums,curr,p2);
                --p2;
            }
            else
                ++curr;
        }
    }
    
    private void swap(int[] A, int i, int j){
        int temp=A[i];
        A[i]=A[j];
        A[j]=temp;
    }
}
```

## [324 Wiggle Sort II](https://leetcode.com/problems/wiggle-sort-ii/)

> Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

也就是说我们要把数组排序成波浪的形式：
```
(even)
  .   .   .   .
 / \ / \ / \ / 
'   '   '   '  
(odd)
  .   .   .   
 / \ / \ / \  
'   '   '   ' 
```
首先按照基本想法，如果我们先把整个数组排序，波浪下面的放前 (n+1)/2 个，上面放 (n-1)/2 个。

我们假设现在有一个排序好的数组： `_ _ _ _ _ _ _`，那么：
```
(odd)(数字为索引值)
  4   5   6   
 / \ / \ / \  
0   1   2   3 
(even)
  4   5   6   7
 / \ / \ / \ / 
0   1   2   3 
```

什么时候是有效呢？如果数组是完全升序的，那么一定有效，会出现问题是因为会出现`nums[i]=nums[i+1]`，即中位数太多，导致排不开，而只要中位数的个数小于波浪上面的个数，就一定能排的开。

先把奇数个的拿出来看

```
(odd)(数字为索引值)
  4   5   6   
 / \ / \ / \  
0   1   2   3 
```

其实我们只要保证中位数排开了不交叉（放在 3，4，5 中），其他两边的顺序不重要，也就是说我们的数组不需要完全排好序的（不需要 nlogn），只要是`[..<mid..]+[..mid..]+[..>mid..]`这种形式就可以，而这种排序方式就是上面的三色排序问题，时间复杂度 `O(n)`。

那我们再看偶数个的行不行

```
(even)
  4   5   6   7
 / \ / \ / \ / 
0   1   2   3 
```

我们发现对于偶数个，如果吧中位数放到(2,3,4,5)中，5 和 2 会出现交叉。为了避开这种情况，我们把顺序转一下

```
(even)
  7   6   5   4
 / \ / \ / \ / 
3   2   1   0
```

这样我们的（2，3，4，5）就不可能出现交叉，也就保证了这个波浪是有效的。

有了三色排序好的数组之后，我们按照一种索引的映射关系，将三色排序的数组映射到我们所需要的数组里面就可以。

假设我们三色排序后的数组为`A`，我们想要的结果的数组是`nums`，映射关系是指对于索引值 `i in A, f(i)=j in nums`。举个例子：

```
(even)
A 中的索引：      7   6   5   4
               /|\ /|\ /|\ /| 
A 中的索引：    3 | 2 | 1 | 0 |
              | | | | | | | |
nums中索引：   0 1 2 3 4 5 6 7

3->0
2->2
1->4
```

这时因为是逆序（i:0->3 = j:6->0)，映射关系比较复杂，我们想能不能把他顺过来。我们看到在波浪中，索引值都是降序的，也就是说如果我们的 A 是从大到小排序，就么映射就顺了。所以我们在处理三色排序的时候，把数组按降序排列：`A=[..>mid..]+[..mid..]+[..<mid..]`，这样波浪索引就变成了:

```
  0   1   2   3
 / \ / \ / \ / 
4   5   6   7
```

这样映射关系就好找多了，大佬们有一个方程来表示这种映射关系： `nums(i)=A[(1+2*(i)) % (n|1)]`

将映射关系带入三色排序里，这样我们表面上是排成`[..>mid..]+[..mid..]+[..<mid..]`这种形式，但其实直接排成了波浪形。

这时还有最后一个问题，如何在 O(n)的时间复杂度里找到中位数？这就又要写一种变相的快排。可见第 [215 Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/).

```Java
class Solution {
    public void wiggleSort(int[] nums) {
        int mid=findKthLargest(nums, (nums.length+1)/2);
        // 3 color sort
        int ma=0, mi=nums.length-1;
        int curr=0;
        int n=nums.length;
        while(curr<=mi){
            if(nums[newIndex(n,curr)]==mid)
                ++curr;
            else if(nums[newIndex(n, curr)]>mid){
                swap(nums, newIndex(n, ma), newIndex(n,curr));
                ++ma;
                ++curr;
            }
            else{
                swap(nums, newIndex(n,mi), newIndex(n,curr));
                --mi;
            }
        }
    }
    // index mapping
    private int newIndex(int n, int i){
        if(i<n/2)
            return 2*i+1;
        return 2*(i-n/2);
    }
}
```

对于找中位数的算法：

```Java
    public int findKthLargest(int[] nums, int k) {
        //if(k>nums.length)   return -1;
        return helper(nums, k, 0, nums.length-1);
    }
    
    private int helper(int[] nums, int k, int left, int right){
        if(left<right){
            int p=partition(nums,left, right);
            if(p+1==k)
                return nums[p];
            else if(p+1>k)
                return helper(nums, k, left, p-1);
            else
                return helper(nums, k, p+1, right);
        }
        return nums[left];
    }
    
    private int partition(int[] nums, int left, int right){
        int pivot=nums[right];
        int p=left, now=left;
        for(; now<right; now++){
            if(nums[now]>pivot){
                swap(nums, p, now);
                ++p;
            }
        }
        swap(nums,p,right);
        return p;
    }
    private void swap(int[] nums, int p, int now){
        int temp=nums[p];
        nums[p]=nums[now];
        nums[now]=temp;
    }
```