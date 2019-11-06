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