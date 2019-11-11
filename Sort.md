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