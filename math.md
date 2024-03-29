## 最大公约数(Greatest common divisor) :green_book:

**欧几里得算法，又叫辗转相除法**基于以下定理：

`gcd(a, b)=gcd(b, a mod b)`

```Java
int gcd(int a, int b){
    if(b==0)
        return a;
    return gcd(b, a%b);
}
```

## 取模运算的运算法则

```
(a+b)%p = (a%p + b%p)%p
(a-b)%p = (a%p - b%p)%p
(a*b)%p = ((a%p) * (b%p))%p
```

## 快速幂算法

已一题目为例：

> 求 A^B 的对 10^9+7 取余后的整数。

这时候对于直接求解来说，最大的问题是溢出。当 B 的取值范围很大时，用 BigInteger 也会有内存溢出（超过限制）的情况。这时候就要用到上面取模运算的第三个规则。

已 3^10 为例，

3^10 = 9^5 = 9 * 9^4 = 9 * 81^2 = 9*6561

我们对指数不断的除以2，底数进行平方运算，当指数为单数时，剥离出一个底数单独相乘。同时应用上述运算法则的第三个不断的进行取模。这样就可以在不出现溢出的情况下以 log(B) 的时间复杂度求解。

```Java
int base = 3;
int power = 1000000000;
int mod = 1000000007;
int result = 1;
while(power > 0) {
    if (power & 1 == 1) { // power 是单数
        result = (result * base) % mod; // 单独乘以底数
    }
    base = (base*base)%mod; // 底数变平方
    power >>= 1; // 指数除以2
}
return result;
```

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

## [523 Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/)

> Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to a multiple of k, that is, sums up to n*k where n is also an integer.

I met a similar problem checking whether there is a continuous subarray sum that is a specific number. This question is to check whether the sum is a multiple of a specific number. When it comes to check the multiple times of a number, we need to pay attention to the modulus.

Let's say `Si` is the sum from 0th to ith, `Sj` is the sum of 0th to jth, if `Sj-Si` is a multiple of k, than `Si` and `Sj` must have a same modulus of k.

We traverse the array and using a hashmap to store the sum from begining to current index. Because we only need to see the modulus, we let `sum=sum%k` and store the sum. When we met a sum that is already in the hashmap, we know that there is a subarray sum meet the requirement.

Java

```Java
class Solution {
    public boolean checkSubarraySum(int[] nums, int k) {
        // 2 corner cases:
        // k<0, so when we put k in calculation, we need to get the absolute value, no, no need. what we need is modulus, no matter the divisor is negative or positive
        // k=0 now I particularly write a part of code to deal with this situation. But it is better to put it in general process.
        int sum=0;
        Map<Integer, Integer> map=new HashMap();
        map.put(0,-1);
        for(int i=0; i<nums.length; ++i){
            sum+=nums[i];
            if(k!=0)
                sum=sum%k;
            if(map.containsKey(sum)){
                if(i-map.get(sum)>1)
                    return true;
            }
            else{
                map.put(sum, i);
            }
        }
        return false;       
    }
}
```
C++

```cpp
class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        // firstly I consider k=0 and k!=0 separatly, but the answer is smarter. if k=0, we just need to see if the sum at ith and the sum at jth is the same.
        // there is no need to get the sum and modulus separatly. they are the same thing to show that whether the get the n*k. we just need the modulus.
        // In order to clean the code, like to see if the index is bigger than 1, we set [0, -1] into the map to make it unified
        map<int, int> dic;
        dic[0]=-1;
        int sum=0;
        for(int i=0; i<nums.size(); ++i){
            sum+=nums[i];
            if(k!=0)
                sum=(sum%k);
            if(dic.find(sum)!=dic.end()){
                if(i-dic[sum]>1)
                    return true;
            }
            else{
                dic[sum]=i;
            }
        }
        return false;
    }
};
```

## [825. Friends Of Appropriate Ages](https://leetcode.com/problems/friends-of-appropriate-ages/)    :triangular_flag_on_post: 

```Java
class Solution {
    public int numFriendRequests(int[] ages) {
        if(ages.length<=1)  return 0;
        int n=ages.length;
        int[] agesNum=new int[121];
        for(int i=0; i<n; ++i){
            agesNum[ages[i]]++;
        }
        int count=0;
        for(int i=0; i<121; ++i){
            for(int j=0; j<121; ++j){
                if(makeFriend(i,j)){
                    if(i==j)
                        count+=(agesNum[i]*(agesNum[i]-1));
                    else{
                        count+=agesNum[j]*agesNum[i];
                    }
                }
            }
        }
        return count;
    }
    public boolean makeFriend(int A, int B){
        if(B<=0.5*A+7 || B>A)
            return false;
        return true;
    }
}
```

## [7 Reverse Integer](https://leetcode.com/problems/reverse-integer/) :green_book:

**Question to ask:**
1. What if the integer's last digit is 0? for example, x=10,100...
2. What if the reversed integer overflows?

We do not need to handle negative integers separately, because the modulus operator works for negative integers as well (e.g., -43%10=-3)

To check for overflow, we could check if ret>214748364 or ret<-214748364 before multiplying by 10. On the other hand, if ret==214748364, it must not overflow because the last reversed digit it guaranteed to be 1 due to constraint of the input x.

```Java
class Solution {
    public int reverse(int x) {
        int ans=0;
        int maxDiv10=Integer.MAX_VALUE/10;
        while(x!=0){
            if(Math.abs(ans)>maxDiv10)
                return 0;
            ans=ans*10+x%10;
            x/=10;
        }
        return ans;
    }
}
```

## [1363 Largest Multiple of Three](https://leetcode.com/problems/largest-multiple-of-three/)

> Given an integer array of digits, return the largest multiple of three that can be formed by concatenating some of the given digits in any order.

> Since the answer may not fit in an integer data type, return the answer as a string.

> If there is no answer return an empty string.

用余数来做这道题这一点想到了，但之前想的是吧余 1 和余 2 的数挑出来，然后点再在这里面 pick，
但这里就有个问题解决不了：如何 pick 能得到想要的结果。
正确的思路是你把全部数加起来，看看余几，然后减去余这个数的最小的数不久完了。fuck