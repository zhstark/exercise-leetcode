## [50 Pow(x, n)](https://leetcode.com/problems/powx-n/) :triangular_flag_on_post:

> Implement pow(x, n), which calculates x raised to the power n (x^n).

1. cornor case: What if x<0? x=0? x>0?
2. `a^n=a^(n/2) * a^(n/2)                 if n is even`
3. `a^n=a^((n-1)/2) * a^((n-1)/2) * a     if n is odd`

C++

When using `abs()` function, we cannot give it an integer type because it will return an integer type and it does not work if input is `-2^n`.

```cpp
class Solution {
public:
    double myPow(double x, int n) {
        if(x==0)    return 0.0;
        
        // using abs() has a problem that there will be an error if n= -2^n
        long long N=n;
        double absPow=myAbsPow(x, abs(N));
        return n<0? 1/absPow: absPow;
    }
private:
    // -2147483648 cannot be represented in type 'int'
    double myAbsPow(double x, unsigned int n){
        if(n==0)    return 1.0;
        if(n==1)    return x;
        
        double half=myAbsPow(x, n/2);
        // 注意优先级
        if((n&0x1)==0)  return half*half;
        return half*half*x;
    }
};
```

## Problem 991 Broken Calculator

On a broken calculator that has a number showing on its display, we can perform two operations:

Double: Multiply the number on the display by 2, or;
Decrement: Subtract 1 from the number on the display.
Initially, the calculator is displaying the number X.

Return the minimum number of operations needed to display the number Y.

这个题应该倒着想，从只有减法和乘法，变为 Y->X，只有加法和除法。因为先减再乘，减法的效果会翻倍，而先加再除，加法的效果会缩小一半。

Opertation 1: Y = Y / 2 if Y is even
Opertation 2: Y = Y + 1


**Explanation**:
Obviously,
If Y <= X, we won't do Y / 2 anymore.
We will increase Y until it equals to X

So before that, while Y > X, we'll keep reducing Y, until it's smaller than X.
If Y is odd, we can do only Y = Y + 1
If Y is even, if we plus 1 to Y, then Y is odd, we need to plus another 1.
And because (Y + 1 + 1) / 2 = (Y / 2) + 1, 3 operations are more than 2.
We always choose Y / 2 if Y is even.


**Why it's right**
Actually, what we do is:
If Y is even, Y = Y / 2
If Y is odd, Y = (Y + 1) / 2

We reduce Y with least possible operations, until it's smaller than X.

And we know that, we won't do Y + 1 twice in a row.
Becasue we will always end with an operation Y / 2.

2N times Y + 1 and once Y / 2 needs 2N + 1 operations.
Once Y / 2 first and N times Y + 1 will end up with same result, but needs only N + 1 operations.

```py
def brokenCalc(self, X, Y):
        res = 0
        while X < Y:
            if Y%2: Y += 1
            else: Y /= 2
        return res + X - Y
```