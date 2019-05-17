## 232 Implement Queue using Stacks

[link](https://leetcode.com/problems/implement-queue-using-stacks/)

> Implement the following operations of a queue using stacks.

> push(x) -- Push element x to the back of queue.
> pop() -- Removes the element from in front of queue.
> peek() -- Get the front element.
> empty() -- Return whether the queue is empty.

Using 2 stacks, stack1 to push, stack2 to pop.

When pushing elements, just push it into s1. When getting the front element, we push all elements from s1 into s2 (assuming now s2 is empty). Then elements in s2 are in reverse order, which is what we want.

If we still want to get the front element(`pop(), peek()`), we just get it from s2 until s2 is empty. Then we pour all elements of s1 into s2 again.

```cpp

class MyQueue {
private:
    stack<int> s1;
    stack<int> s2;
public:
    /** Initialize your data structure here. */
    MyQueue() {

    }
    
    /** Push element x to the back of queue. */
    void push(int x) {
        s1.push(x);
    }
    
    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        if(s2.empty()){
            while(!s1.empty()){
                s2.push(s1.top());
                s1.pop();
            }
        }
        int temp=s2.top();
        s2.pop();
        return temp;
    }
    
    /** Get the front element. */
    int peek() {
        if(s2.empty()){
            while(!s1.empty()){
                s2.push(s1.top());
                s1.pop();
            }
        }
        return s2.top();
    }
    
    /** Returns whether the queue is empty. */
    bool empty() {
        return s1.empty() && s2.empty();
    }
};
```