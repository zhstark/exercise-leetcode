## 链表常用技巧

一个 slow 指针一个 fast 指针遍历，这样指到中间的节点。

这里技巧是 slow 和 fast 都从头开始，检测 fast.next 和 fast.next.next。

**如果让 slow 停留在考前一点的位置:**

```Java
public ListNode mid(ListNode head){
    if(head==null)  return head;
    
    // head!=null, head.next!=null
    ListNode slow=head;
    ListNode fast=head;
    while(fast.next!=null && fast.next.next!=null){
        slow=slow.next;
        fast=fast.next;
    }
    return slow;
}
```

## 用 dummy node

- when the head could be changed when solving the problem
- not sure yet which node will be head when constructing the list

eg. insert a value into a sorted list
eg. merge 2 sorted linked list.

对链表增删改。

return dummy.next

## 反转链表

从当前节点开始，返回开始前链表的最后的一个节点，即反转后的头节点

```py
#准备反转
curr=slow
pre=None     

# 反转链表
while curr:
    n=curr.next
    curr.next=pre
    pre=curr
    curr=n

head2=pre
```

Recursion:

```Java
class Solution{
    public Node reverse(Node root){
        if(root == null || root.next == null){
            return root;
        }

        Node newHead = reverse(root.next);
        root.next.next = root;
        root.next = null;
        return newHead;
    }
}
```

----

```cpp
//Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};
 ```

## [23 Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)   :triangular_flag_on_post:

> Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

The methods used to solve this problem are [priority queue](Stack&Queue.md) and [divide and conquer](Divide&Conquer.md). The time complexity are both O(Nlogk). See the details in these 2 files.

## [92 Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/)

> Reverse a linked list from position m to n. Do it in one-pass.

> Note: 1 ≤ m ≤ n ≤ length of list.

```Java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode reverseBetween(ListNode head, int m, int n) {
        if(head==null)  return null;
        if(m>=n)    return head;
        ListNode pre=null;
        ListNode curr=head;
        int dis=n-m;
        for(int i=0; i<m-1; i++){
            ListNode next=curr.next;
            pre=curr;
            curr=next;
        }
        
        ListNode pre2=null;
        ListNode head2=curr;
        for(int i=0; i<dis; ++i){
            ListNode next=curr.next;
            curr.next=pre2;
            pre2=curr;
            curr=next;
        }
        if(pre!=null)
            pre.next=curr;
        else
            head= curr;
        head2.next=curr.next;
        curr.next=pre2;
        return head;
    }
}
```

## [86 Partition List](https://leetcode.com/problems/partition-list/)

> Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

> You should preserve the original relative order of the nodes in each of the two partitions.

The intuition is to use 2 pointers -- small and big to traverse the linked list and record all the nodes which are samller than x and which are big than x. This step split the whole linked list into 2 sub linked list.

Then we joint these 2 linked list together, than the final linked list will meet the requirement.

```Java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode partition(ListNode head, int x) {
        ListNode node1=new ListNode(0);
        ListNode node2=new ListNode(0);
        ListNode small=node1;
        ListNode big=node2;
        while(head!=null){
            if(head.val<x){
                small.next=head;
                small=small.next;
            }
            else{
                big.next=head;
                big=big.next;
            }
            head=head.next;
        }
        big.next=null;
        small.next=node2.next;
        return node1.next;
    }
}
```