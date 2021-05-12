## 做题要点

1. Document your assumption
2. Explain your approach and how you intend to solve the problem
3. Provide code comments where applicable
4. Explain the big-O run time complexity of your solution. Justify your answer.
5. Identify any additional data structures you used and justify why you used them
6. Only provide your best answer to each part of the question.
7. when use '/', consider about precision for integer, denominator（分母）=0

High level

## Recursion

实质上：Boil down a big problem to smaller ones (size n depends on size n-1, or n-2...)

implementation:
1. base case
2. Recursive role

## Queue:

common use:
1. Tree printout by level
2. sliding  window problems

## Stack

什么问题要往 Stack 上考虑
Answer： 从左往右 linear scan 一个 array/string 时，如果要不断回头看左边最新的元素时，往往要用 stack
1. Histogram 中最大长方形
2. reverse polish notation 逆波兰表达式的计算 a*(b+c) ->abc+*
3. String 的 repeatedly deduplication, cabba -> caa -> c

## Linked list

1. When you want to de-reference a listNode, make sure it is not a NULL pointer
2. Never ever lost the control of the head pointer of the LinkedList
3. Be care about 2 corner case: head and tail

## Tree

树的三部曲：
1. ask for something from the left and right children
2. do something at the current level/node
3. report to the current node's parent, ensure the 物理意义 is the same as step 1

base case usually refer to the null childNode below the leaf node

Balanced binary tree: is commonly defined as a binary tree in which the depth of the left and right subtrees of every node differ by 1 or less

complete binary tree: is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.

## Heap(Priority queue)

Heap: is an unsorted array but have special rules to follow

最小堆：min-heap

heapify: 使得一个 unsorted array 变成一个堆： time complecity: O(n)

*Q1*: Find smallest k elements from an unsorted array of size n

How to make assumptions?
   1. what is the relationship between k and n???

Solution1:
    sort it and return the first k element   O(nlogn)

Solution2:
    step1: how to build a min-heap? --> heapify it O(n)
    step2: keep popping out k elements --> O(klogn)
    totoal time = O(n+klog(n))

Solution3:
    step1: use a max-heap of size k   O(k)
    Step2: iterate from the k+1th to the nth elements, and for the current element X
    case1: if X < max-heap.top()

## Graph

### BFS1 BFS2

什么时候用 Breath First Search？
1. when we deal with the tree-related problem and in the meantime we need to address the **relationship on the same level**

Best First Search: 
1. Dijkstra's Algorithm (点到面（所有点)的最短距离算法):
   1. Data structure: priority queue （min heap)
   2. 思路：
      1. initial state (start node)
      2. Node expansion/Generation rule
      3. Termination condition: 所有点都计算完毕才停止，也就是 pq 变空
   3. properties:
      1. *all the cost of the nodes that are expanded are monotonically non-decreasing*
      2. time complexity O(nlogn)
      3. when a node is popped out for expansion, its value is fixed which is equal to the shortest distance from the start node.

### DFS

在一个 function 里面调用自己两次或两次以上

基本方法：
1. what does it store on each level?（每层代表什么意义？一般来讲解题之前就知道 DFS 要 recurse 多少层）
2. How many different states should we try to put on this level？（每层有多少个状态/case/ 需要 try）

## Hash Table

**See wiki for basic knowledge**

when u use hash table, tell what's the key and what's the value

## String

1. Removal
   1. remove some particular chars from a string
   2. remove all leading/trailing/duplicated empty spaces from a string
2. De-duplication aaaaaabbbb_ccc -> ab_c
3. Replacement
4. Reversal (swap) e.g. I love yahoo -> yahoo love I
5. Substring -> strstr
   1. regular method
   2. Robin-Carp & KMP
6. Move letters around e.g. ABCD1234 -> A1B2C3D4
7. Permutation (use DFS)
8. decoding/encoding
9. sliding windows usin slow/fast pointers
   1.  longest substring that contains only unique chars abcda

Example: I Love Yahool --> Yahool love I，互换 word 位置 -- 两遍 reverse

思想：
1. 两个挡板
2. 两遍 reverse

描绘一个复杂算法：
1. 要用哪些变量，分别代表什么

## Bit

负数表示：变反，+1

## OOD Object Oriented Design

why:
1. Practical problems -> Model -> Code
2. Better understanding of OOP
3. Code details

What is good code? What is a good design?
1. Complete functionality
2. Easy to use
   1. Clear, elegant, easy to understand, no ambiguity
   2. Prevent usrs from making mistakes
3. Easy to evolve

Class inheritance: do we need to use protected for methods attributs
   a. Protected methods: sometimes useful when we want to override an implementation in subclasses
   b. Protected attributes: be careful, try to use private first

Polymorphism（多态）

### Eg. design a parking lot

不要先想这东西是什么，先考虑有什么功能（**核心功能**）--> API 。即这个东西能干什么，核心功能是什么，然后推导出 API，这些 API 的输入是什么，输出是什么

1. Understand/Analyze the use case: Describe the parking log building? Vehicle monitoring? What kind of parking lot? (明确这个程序是干嘛的)

For **API**, always ask yourself: **input/output**?

Some other questions that may affect your design:
One level or multiple levels?
Parking-spot / Vehicle sizes?
Track the location of each vehicle?

2. Classes and their relationship 列出用到的 class 并理清他们之间的关系

Single-responsiblity Principle: A class should has only one job

Vehicle, Parking Spot, Level, ParkingLot...

class relationships:
- Association: a general binary relationship that describes an activity between two classes
- Aggregation/Composition: a special form of assocations, which represents an ownership relationship between 2 classes

Vehicle -- Parking spot
Level -- Parking Spot
Parking Lot -- Level
Vehichle -- Car, Truck

Functionality:
1. Basic functionlity: for a given vehicle, tell whether there is avaliable spot in the parking log.
2. Possible extensions: provide available spot locations, assign spot to the vehicle

Assumption:
1. multiple levels
2. check vehicle size

APIs:
boolean hasSpot(Vehicle v);
boolean park(Vehicle v);
boolean leave(Vehicle v);

classes:
ParkingLot, Level, Vehicle, ParkingSpot, Car, Truck

```
public enum VehicleSize {
   Compact, Large
}

public abstract class Vehicle {
   public abstract VehicleSize getSize();
}

// Car class
public class Car extends Vehicle {
   @Override
   public VehicleSize getSize() {
      return VehicleSize.Compact;
   }
}

```

### Builder pattern

1. class 中包括有很多个 data fields
2. class 中有些 fields 可以不在 constructor 里初始化（optional）

要么一堆 contstructor，要么一堆 setter，调用 setter 才完成 object creation

encapsulation 封装性

```Java
public class User{
   private final String firstName;
   private final Stirng lastName;
   private int age;
   private String phone;
   private String address;

   private User(UserBuilder builder) {
      this.firstName = builder.firstName;
      this.lastName = builder.lastName;
      this.age = builder.age;
      this.phone = builder.phone;
      this.address = builder.address;
   }
   // 为什么 static，如果不 static，就得先有 user 再有 builder
   public static class UserBuilder {
      private final String firstName;
      private final Stirng lastName;
      private int age = 0;
      private String phone = "";
      private String address;

      public UserBuilder(String firstName, String lastName) {
         this.firstName = firstName;
         this.lastNmae = lastName;
      }

      // all the following methods are used to set values for optional fields
      public UserBuilder age(int age) {
         this.age = agel
         return this;
      }

      public UserBuilder phone(String phone) {
         this.phone = phone;
         return this;
      }

      public UserBuilder address(String address) {
         this.address = address;
         return this;
      }

      public User build() {
         return new User(this);
      }
   }
}

public static void main() {
   User user = new UserBuilder("Tin", "Stark")
                              .age(18)
                              .phone("131321");
                              .build();
}
```

### Factory pattern

class 17

吧 object creation 的逻辑和 usage 分离

1. separate instance/object creation logic from its usage
2. more clean especially when we have complicated instace
3. 重用

### Singleton

Ensure a class has only one instance, and provide a global point of access to it.

**必须要会**

```Java
public class Singleton {
   private static final Singleton INSTANCE = new Singleton();

   private Singleton() {}

   public static Singleton getInstance() {
      return INSTANCE;
   }
}
```



## DP

类似于数学归纳法，把一个大问题的解决方案用比他小的问题来解决。

与 recursion 的关系：
1. Recursion 从大到小来解决问题问题，不记录任何 sub-solution 只考虑
   1. base case
   2. recursion rule
2. DP 从小到大来解决问题，记录 sub-solution
   1. 有 size（\<n）的 subsolution（s） -> size(n) 的 solution
   2. base case
   3. induction rule

**Concept:**
- sub-array: contiguous elements in an array
- sub-sequence: not necessarily  contiguous

### largest sum of subarray

```Java
class Solution {
   public int largestSum(int[] array) {
      if (array == null || array.length == 0) {
         return 0;
      }
      int largest = array[0];
      int sum = 0;
      for (int i = 0; i < array.length; i++) {
         if (sum < 0) {
            sum = array[i];
         } else {
            sum += array[i];
         }
         largest = Math.max(largest, sum);
      }
      return largest
   }
   // return the subarray index
   public int largestSum2(int[] array) {
      if (array == null || array.length == 0) {
         return 0;
      }
      int left = 0;
      int sol_left = 0;
      int sol_right = 0;
      int global_max = Integer.MIN_VALUE;
      int sum = 0;
      for (int i = 0; i < array.length; i++) {
         if (sum < 0) {
            sum = array[i];
            left = i;
         } else {
            sum += array[i];
         }
         if (sum > global_max) {
            global_max = sum;
            sol_left = left;
            sol_right = i;
         }
      }
      return global_max;
   }
}
```

## Probability, Sampling, Randomization

shuffling poker algorithm
1.1 spades  黑桃
1.2 hearts  红心
1.3 diamonds   方片
1.4 clubs   梅花

suit 花色




Random(5) --> Random(7)

升维

```
            r2 
      0 1 2 3 4 
r1=1  5 6 7 8 9 
      10 11 12 13 14
      15 16 17 18 19
      20 21 22 23 24 
```

call random(5) for the 1st time = random(0-4) -> row number
call random(5) for the 2nd time = random(0-4) -> col number

generated_number = r1*5+r2

## Systen Design

### Distributed File System

1. learn the correct design steps(e.g. Use case -> functionality -> Architecture ....)
2. Preparation:
   1. Basic database/network/OS knowledge
   2. Basic knowledge about system in practice


Topics will cover:
1. Storage
   1. Distributed file system
   2. Distributed database
2. Computation
   1. Batch Parocessing
   2. Stream Processing
3. Web applications

1. use file system inferfaces to manage your data
2. data is distributed in many machines
3. e.g. GFS, HDFS
4. when to use a DFS