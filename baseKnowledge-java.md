## Basic

一个 Java 文件一个 `public class` 且类名和文件名一样，可有多个 `class`，这些 class 仅限 package 内可见(helper class)。

## Array vs Linked List

- memory layout
	- Array: consecutive allocated memory space, no overhead.
	- LinkedList: non-consective, overhead of multiple objects withe `next` reference
- (Random) access time? - get ith element
    - Array: O(1) -> calcuting the offset is O(1)
    - LinkedList: O(n) worst case -> we can only traverse from the `HEAD`
- Search time (non-sorted)?
    - Array: O(n);
    - LinkedList: O(n)
- Search time (sorted)
    - Array: O(logn) -> binary search
    - LinkedList: O(n)
    - **Reason**: random access time is different for array and list

**things to keep in mind**

1. check null
2. check length/size/head==null/head.next==null/other initial check conditions
3. check index out of bound/NullPointer(even inside the for/while loop)
   1. keep in mind any idex can not be out of range (<0 || >=array.length)
   2. keep in mind some ListNode reference might be null
4. What is the termination conditio of for/while loop
5. Make some concrete examples to determine if the logic is correct

## 做题要求

A complete answer will include the following:
1. Document your assumptions
2. Explain your approach and how you intend to solve the problem
3. Provide code comments where applicable
4. Explain the big-O run time complexity of your solution. Justify your answer.
5. Identify any additional data structures you use and justify why you used them.
6. Only provide your best answer to each part of the question.

讲 code：highlevel

从第 0 行 signature 开始讲

## Stack & Deque & Queue

**不要再使用 Stack class，转用 LinkedList 替代**

最常用的：LinkedList, ArrayDeque.

ArrayDeque: 不许存 null

Queue：offer(), poll(), peek()
add(), remove(), element() 需要处理异常

```Java
Deque<Integer> stack=new LinkedList<>();
stack.offerFirst(1);
stack.offerFirst(2);
while(!stack.isEmpty()){
    System.out.println(stack.peekFirst());
    System.out.println(stack.pollFirst());
}
```

**Circular array**: we can connect the start and end of the array, so that it is a cycle. index of array.length <=> index of 0.

head=head+1==array.length? 0: head+1; //(head+1)%array.length;

## Tree

```Java
class TreeNode{
    int key;
    TreeNode left;
    TreeNode right;

    public TreeNode(int key){
        this.key=key;
    }
}
```

### Binary Search Tree

For any of the nodes in the binary tree, all the nodes in its right subtree is larger than itself, all the nodes in its left subtree is smaller than itself.

Balanced Binary Search Tree

Search(), insert(), remove() operations are all guaranteed to be O(logn)

Red-Black tree:
    - in Java: TreeMap/TreeSet
    - in C++: map/set

为什么 BST 不考虑重复的情况。

- inorder
- preorder
- postorder
- levelorder

Why iterative? Stack overflow if the tree is very deep. The recursion is internally done by using STACK to maintain the method call levels and directions, we can simulate this ourselves, so a stack will be needed.

> Stack: storing the local variables and other info for each of the method calls
> Heap: allocating spaces for dynamiccly created objects

#### pre-order

```Java
class Solution{
    public List<Integer> preOrder(TreeNode root){
        List<Integer> ans=new ArrayList<>();
        if(root==null){
            return ans;
        }
        Deque<TreeNode> stack=new LinkedList<>();
        stack.offerFirst(root);
        while(!stack.isEmpty(){
            TreeNode node=stack.pollFirst();
            ans.add(node.val);
            if(node.right!=null){
                stack.offerFirst(node.right);
            }
            if(node.left!=null){
                stack.offerFirst(node.left);
            }
        }
        return ans;
    }
}
```

#### in-order

How can we know we have already traversed all the nodes in left sub?

每次都先沿着左子树把这条线都遍历到头。

use a helper node to store the next "visiting" node and subtree

1. when helper node is not null, we should traverse the subtree, so we push helper and we go left.
2. when helper is null, means the left subtree of the root is finished, the root is the top element in the stack. We can print the top, and let helper=top.right(traverse the left subtree first, then top, the right subtree)
3. do 1 and 2 until helper is null the there is no node left in the stack

```Java
class Solution{
    public List<Integer> inOrder(TreeNode root){
        List<Integer> ans= new ArrayList<>();
        if(root==null){
            return ans;
        }
        TreeNode helper=root;
        Deque<TreeNode> stack=new LinkedList<>();
        while(helper!=null || !stack.isEmpty()){
            if(helper!=null){
                stack.offerFirst(helper);
                helper=helper.left;
            }
            else{
                TreeNode node=stack.pollFirst();
                helper=node.right;
                ans.add(node.val);
            }
        }
        return ans;
    }
}
```

#### post-order

**Need to know the direction. Maintain a previour node to record the previous visiting node on the traversing path,** so that we know what the direction we are taking now and what is the direction we are taking next.

- root=stack.top
- if previous is null --> going down left
- if previous is current's parent --> going down left
- if previous == current.left --> left subtree finished, going donw right
- if previous == currnet.right --> right subtree finished, pop current, going up

```Java
public void postOrder(TreeNode root){
    if(root==null){
        return;
    }
    Deque<TreeNode> stack=new LinkedList<>();
    TreeNode pre=null;
    stack.offerFirst(root);
    while(!stack.isEmpty()){
        TreeNode curr=stack.peekFirst();
        if(pre==null || pre.left==curr || pre.right==curr){
            if(curr.left!=null){
                stack.offerFirst(curr.left);
            }
            else if(curr.right!=null){
                stack.offerFirst(curr.right);
            }
            else {
                System.out.println(curr.val);
                stack.pollFirst();
            }
        }
        else if(pre==curr.left){
            if(curr.right!=null){
                stack.offerFirst(curr.right);
            }
            else{
                System.out.println(curr.val);
                stack.pollFirst();
            }
        }
        else{
            System.out.println(curr.val);
            stack.pollFirst();
        }
        pre=curr;
    }
}
```

## Map & Set

Time complexity: **average O(1) but worst O(n)**

### HashMap

- V put(K, V)
- V get(K)
- V remove(K)
- boolean containsKey(K)
- Set<Map.Entry<K,V>> entrySet() - get the set view of all the entries in the hashmap
- Set<K> keySet() - get the set view of all the keys in the hashmap
- Collection<V> values() - get the collection view of all values in the hashmap
- boolean containsValue(V) - O(n)
- void clear()
- int size()
- boolean isEmpty() 

**一定要保存 key!**

Entry<K, V>[] array: hashmap bucket 的 数组

array[i] is the head of the linkedlist

HashMap use `key.hashCode()` to determine the entry index for the key, `key.equals()` to determine whether two keys are the same keys.

**When you want to override equals(), please definitely override hashCode() as well**

```Java
Iterator<Map.Entry<String, Integer>> iter=map.entrySet().iterator();
while(iter.hasNext()){
    Map.Entry<String, Integer> cur=iter.next();
    if(cur.getValue()==0){
        iter.remove();
    }
}

```

### HashSet

- boolean add(E e) // return true if this set did not already contain the specified element
- boolean remove(E e)
- boolean contains(E)
- void clear()
- int size()
- boolean isEmpty()

## String

- make the requirement clear, is it allowed to use some of the very efficient jave utilities
    - Can ues StringBuilder?
    - Can use the existing method in String? e.g. trim(), replace()
- Usually 2 strategies
    - char[] array=input.toCharArray()
    - use StringBuilder

## OOP

### Override vs Overload

override is when u redefine a method  that has been defined in a parent class(using the same signature). Resolved at runtime.

Overload is when  define 2 methods with the same name, in the same class, distinguish by their signatures (different), resolved at compile time

### Interface vs abstract class

A class must be declared abstract when it has one or more abstract methods. A method is declared abstract when it has a method heading, but no body.

```Java
public abstract class Figure{
    public abstract float getArea();
    public void print(){
        System.out.println("This is a figure");
    }
}
public class Circle extends Figure{
    private float radius;
    public float getArea() {
        return (3.14*(radius*radius));
    }
}
```

An interface differs from an abstract class has only abstract methods

```Java
public interface CanBark{
    public void bark();
}
public class Husky implements Canbark{
    public void bark(){
        System.out.println("wwwww");
    }
}
```

Java 不许有多重继承，可以同时实现多个 interface

Interview Question: When will you use abstract class vs. interface? 

> An abstract class is good if you think you will plan on using inheritance since it provides a common base class implementation to derived classes

> An abstract class is also good if you want to be able to declare non-public mumbers. In an interface, all methods must be public. If you think you will need to a dd methods in the future, then an abstract class is a better choice. Because if you add new method headings to an interface, then all of the classes that already implement that interface will have to be changed to implement the new methods.

> Interfaces are good choice when you think that the API will not change for a while. Interfaces are also good when you want to have something similar to multiple inheritance, since you can implement multiple interfaces.

abstract: is a;
interface: has a function

### Access modifier

- public: everyone can access
- private: only myself can access
- protected: only my children and same package can access
- default: only the same package can access


| Modifier | class | package | subclass | world |
|-----|-----|-----|-----|-----|
| public | Y | Y | Y | Y | 
| protected | Y | Y | Y | N | 
| no modifier | Y | Y | N | N | 
| private | Y | N | N | N | 

### Exception & Error

An exception indicates conditions that a reasonable application might want to catch. (因不可抗力导致的程序执行过程中发生的意外)

An Error indicates serious problems that a reasonable application should not try to catch: StackOverflowError. Both Error and Exceptions extend from Throwable.

**Finally** will always be executed, even with a return. (But not System.exit(0))

```Java
try{
    ...
    return;
} catch (Exception e){
    ...
} finally {
    System.out.println("Finally");
}
```

### Nested Class

```Java
class OuterClass{
    static class NestedStaticClass{ //这样的类不是属于一个 instance 的
    }

    class InnterClass{ // 属于一个 instance
    }
}

OuterClass outer=new OuterClass();
OuterClass.InnerClass inner=outer.new InnerClass();
OuterClass.InnerClass inner2=(new OuterClass()).new InnerClass();
```

Inner class: 一个类根植于一个 instance，can access both static and non-static members of Outer class.

A static class cannot access non-static members of the Outer class. I can access only static member of Outer class.

**Anonymous inner class(defined in a method with just new and no definition)**

```Java
public class AnonymousInnerClass{
    public void test(){ // Runnable is an interface
        new Thread(new Runnable(){
            @Override
            public void run(){
            }
        }).start();

        // non anonymout
        class NoneAnoymousClass implements Runnable{
            public void run(){
            }
        }
        NoneAnoymoutCLass t=new NoneAnoymoutCLass();
        new Thread(t).start();

        new Thread(->{
            System.out.println("Hello from Lambda!");
        }).start();
    }
}
```

### Iterator

Iterator through a Collection object (List, etc.)
- next(): Returns the next element in the iteration
- hasNext(): Returns true if the iteration has more elements
- remove(): Removes from the underlying collection the last element returned by this iterator

```Java
List<Integer> list = new LinkedList<>();
for(int i=0; i<list.size(); i++){
    System.out.println(list.get(i));
}

for(Iterator<Apple> iter=list.iterator(); iter.hasNext(); ){
    Apple apple= iter.next();
    System.out.println(apple.printOut());
}

for(int i: list){...}  // foreach, 自动使用 iterator

for(Iterator<String> it = list.iterator(); it.hasNext(); ){
    String str=it.next();
    it.remove(); 
}
```

**ListIterator** A ListIterator has no current element; its cursor position always lies between the element that would be returned by a call to previous() and the element that would be returned by a call to next()
- previous()
- previousIndex()
- hasPrevious()
- nextIndex()

Exercise: Iterator on binary trees

### Generics 泛型

**Definition**
Types are parameters 把类型作为参数
A type or method to operate on objects of various types while **providing compile-time type safety**.

```
f(x)={
    int square(int x){
        return x*x;
    }
}

F(x y)={
    y square(y x){
        return x*x;
    }
}
F(5, double）=double square(double 5.0)=>25.0 
```

```Java
public interface List<T> extends Collection<T>{
    T get(int index);
}

public interface Entry<K, T>{
    K getKey();
    V getValue();
}

//Static method
public static <T> T getFirst(List<T> list){
    ...
}
```

### Enum

**管理**常量、常对象

```Java
public static clas RainbowColor{
    public static final int RED=0;
    public static final int ORANGE=1;
    public static final int YELLOW=2;
    public static final int ...
    public static final int ...
    public static final int ...
    public static final int ...
}

//instead we can
enum RainbowColor{RED, ORANGE, YELLO, GREEN,..}

public enum WeekDayEnum{Mon, Tue, Wed, Thu, Fri, Sat, Sun}

WeekDayEnum today=readToday();

switch(today){
    case Mon:..
    case Tue:...
    ....
}
```
