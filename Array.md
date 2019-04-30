## 287 Find the duplicate number

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

**You must not modify the array (assume the array is read only).**
**You must use only constant, O(1) extra space.**
**Your runtime complexity should be less than O(n2).**

### Solution 1

We can split the figures of 1~n into 2 parts from the middle m. Part one is 1~m, part two is m+1~n. If the numbers of 1~m is more than m, than this part must has the duplicate number. Then we split this part again, like binary search. So the time complexity is O(nlogn), the sapcial complexity is O(1).

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