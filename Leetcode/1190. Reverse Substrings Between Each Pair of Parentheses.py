class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        res, stack = "", []
        for character in s:
            if character == "(":
                stack += [""]
            elif character == ")":
                temp = "".join(stack.pop())[::-1]
                if stack:
                    stack[-1] += temp
                else:
                    res += temp
            elif stack:
                stack[-1] += character
            else:
                res += character
        return res