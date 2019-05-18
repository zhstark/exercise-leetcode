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

Time complexity is pushO(1), pop O(1) amortized,O(n) worst.

*There is another method in which push O(n), pop O(1), not shown*

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

## 225 Implement Stack using Queues

[link](https://leetcode.com/problems/implement-stack-using-queues/)

> Implement the following operations of a stack using queues.

> push(x) -- Push element x onto stack.
> pop() -- Removes the element on top of the stack.
> top() -- Get the top element.
> empty() -- Return whether the stack is empty.

Two methods:

1. push O(n), pop O(1)
2. push O(1), pop O(n)

When push O(n), we can just use 1 queue. Every time we push an element, we push it at back and rotating the queue until the new element is at the front by moving size()-1 front element to the back.

```cpp
class MyStack {
public:
    /** Initialize your data structure here. */
    MyStack() {
        
    }
    
    /** Push element x onto stack. */
    void push(int x) {
        q.push(x);
        for(int i=0; i<q.size()-1; ++i){
            q.push(q.front());
            q.pop();
        }
    }
    
    /** Removes the element on top of the stack and returns that element. */
    int pop() {
        int temp=q.front();
        q.pop();
        return temp;
    }
    
    /** Get the top element. */
    int top() {
        return q.front();
    }
    
    /** Returns whether the stack is empty. */
    bool empty() {
        return q.empty() && q2.empty();
    }
private:
    queue<int> q;

};
```