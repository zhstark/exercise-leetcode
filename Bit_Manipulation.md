## 基本操作
- & and
- | or
- ~ not
- ^ xor(异或,相同为0，相异为1)
- <<,>> 移位操作
  
- 并集：A | B
- 交集: A & B
- A-B: A & ~B
- 将第 x 位置1: A | 1<<x
- 将第 x 位置0: A & ~(1<<x)
- 第 x 位是否为1: A&(1<<x)!=0
- 所有 bit 都是1: -1

## 计算一个数有多少位是1：
```py
def count_one(n):
    count=0
    while n:
        n=n&(n-1)
        count+=1
    return count
```


## 位操作求和
二进制求和 x+y：

| x | y | sum | carry |
|-----|-----|-----|-----|
| 0 | 0 | 0 | 0 |
| 1 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 1 | 0 | 1 |

sum 为其异或， carry 为其与。

多位求和（l_carry 为上一位的进位）：

| x | y | l_carry | sum | carry |
|-----|-----|-----|-----|-----|
| 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 | 1 |
| 0 | 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 | 1 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 | 1 |

`sum=x^y^l_carry`

`carry=x&y or x&l_carry or y&l_carry`

```py
def add(a,b):
    if b==0:
        return a
    else:
        add(a^b, (a&b)<<1)

```

## Gray code

Gray code is a binary numeral system where 2 successive values differ in only one but.

For example, the sequence of Gray codes for 3-bit numbers is: 000, 001, 011, 010, 110, 111, 101, 100, so G(4)=6.

`G(n)=n XOR (n>>1)`

```
int g(int n){
    return n^(n>>1);
}
```

[1238 Circular Permutation in Binary Representation](https://leetcode.com/problems/circular-permutation-in-binary-representation/)


## [137 Single Number II](https://leetcode.com/problems/single-number-ii/)

> Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one. a linear runtime complexity. Could you implement it without using extra memory?

To solve this problem using only constant space, you have to rethink how the numbers are being represented in computers -- using bits.

If you sum the ith bit of all numbers and mod 3, it must be either 0 or 1 due to the constraint of this problem where each number must appear either 3 times or once. This will be the ith bit of that "single number".

A straightforward implemention is to use an array of size 32 to keep track of the total count of ith bit.

```Java 
class Solution {
    public int singleNumber(int[] nums) {
        int[] bits=new int[32];
        int ans=0;
        for(int i=0; i<32; i++){
            for(int j: nums){
                bits[i]+=(j>>i)&1;
            }
            bits[i]=bits[i]%3;
            ans|=(bits[i]<<i);
        }
        return ans;
    }
}
```

We can improve this based on the previous solution using three bitmask variables:
1. ones as a bitmask to represent the $i^th$ bit had appeared once
2. twos as a bitmask to represent the $i^th$ bit had appeared twicn
3. threes as a bitmask to represent the $i^th$ bit had appeared three times

When the $i^th$ bit had appeared for the third time, clear the $i^th$ bit of both ones and twos to 0. The final answer will be the values of ones.

```Java
int singleNumber(int A[]){
    int ones=0, twos=0,threes=0;
    for(int i: A){
        twos |= ones & A[i];
        ones ^=A[i];
        threes=ones&twos;
        ones&=~threes;
        twos&=~threes;
    }
    return ones;
}
```