# =================== Problem 17 ===========
# 迭代的方法关键是更新结果，并且与递归的区别是迭代是倒序，先搞完第一个再搞完第二个
# 递归的关键是找到终止条件和递归公式。


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        m = [" ", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        def recur(digits):
            n = int(digits[0])

            if len(digits) == 1:
                return [x for x in m[n]]
            l = []
            s = m[n]
            letters = recur(digits[1:])
            for letter in s:
                for j in letters:
                    l.append(letter+j)

            return l

        return recur(digits)
