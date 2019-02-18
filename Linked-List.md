## 链表常用技巧

一个 slow 指针一个 fast 指针遍历，这样指到中间的节点。

这里技巧是 slow 和 fast 都从头开始，检测 fast 和 fast.next。

遍历之后可以在符合条件下将 slow 向后移一位，这样当节点为单数时，保证从 slow 开始往后的部分是小的那一部分。

```py
slow=head
fast=head
while fast and fast.next:
    slow=slow.next
    fast=fast.next.next
if fast:
        slow=slow.next
```

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