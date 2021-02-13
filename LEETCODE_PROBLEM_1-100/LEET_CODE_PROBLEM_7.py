"""
Given a signed 32-bit integer x, return x with its digits reversed.

If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Input: x = 123
Output: 321

Input: x = -123
Output: -321

Input: x = 120
Output: 21

Input: x = 0
Output: 0

"""
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            str_x = str(x)
            out = int(str_x[::-1])
        else:
            str_x = str(x)
            out = int('-' + str_x[:0:-1])
        if out > 2**31-1 or -2 ** 31 > out:
            out = 0
        return out
solver = Solution()
print(solver.reverse(1563847412))