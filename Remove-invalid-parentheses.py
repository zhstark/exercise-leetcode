# ===============Problem 301=================
# 1.
# 用 count +1-1计算括号是否合法
# 用两个for 循环遍历所有可能
# 论 filter（）的正确用法


class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isvalid(s):
            ctr = 0
            for c in s:
                if c == '(':
                    ctr += 1
                elif c == ')':
                    ctr -= 1
                    if ctr < 0:
                        return False
            return ctr == 0
        level = {s}
        while True:
            valid = filter(isvalid, level)
            valid = list(valid)
            if valid:
                return valid
            level = {s[:i] + s[i+1:] for s in level for i in range(len(s))}
