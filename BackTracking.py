# ===========================Problem 282==========================
# =========== Expression Add Operators =========
# step1
# 对输入的数字有不同的切分方式，所以要想办法遍历所有可能的组合。
# 类似有分治排序的分割方法，不同是每次分割都会去组合一遍，而不是把全部分割为单个数字后再组合
# 分割过程还要注意“00”的存在

# step2
# 遍历所有+ - * 运算。
# 对于‘*’， 需要保存前面挨着的乘法得到的数（没有乘法运算就是上一个数）
# A+B*C 为上一步的表达式，值为curr， 这一步 *d
# 在上一步要保存 prev=B*C 传递到下一次迭代。
# A+B*C*d=(A+B*C)-prev+prev*d
# 更新 prev=prev*d


class Solution:
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        if not num:
            return []
        self.target = target
        l = []

        for i in range(1, len(num)+1):
            if i == 1 or (i > 1 and num[0] != '0'):
                self.helper(int(num[:i]), int(num[:i]), num[i:],  num[:i], l)

        return l

    def helper(self, pre, curr, num, ans, l):
            if not num:
                if curr == self.target:
                    l.append(ans)
                return

            for i in range(1, len(num)+1):
                if i == 1 or (i > 1 and num[0] != '0'):
                    temp = num[:i]
                    # +
                    self.helper(int(temp), curr+int(temp),
                                num[i:], ans+'+'+temp, l)
                    # -
                    self.helper(-int(temp), curr-int(temp),
                                num[i:], ans+'-'+temp, l)
                    # *
                    self.helper(pre*int(temp), curr-pre+pre *
                                int(temp), num[i:],  ans+'*'+temp, l)
