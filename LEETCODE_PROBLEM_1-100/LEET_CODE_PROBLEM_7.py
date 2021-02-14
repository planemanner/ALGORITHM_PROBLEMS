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
## 시간을 더 적게 사용
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            out = int(str(x)[::-1])
        else:
            out = int('-' + str(x)[:0:-1])
        if out > 2**31-1 or -2 ** 31 > out:
            out = 0
        return out

## 공간 메모리를 더 적게 사용
class other_solution():
    def reverse(self, x):
        q = 1
        nums = []
        out = 0
        if x < 0:
            x = -x
            nums.append('-')
        else:
            nums.append("")
        while q != 0:
            q = x // 10
            residue = x - q * 10
            nums.append(residue)
            x = q

        for idx, num in enumerate(nums[1:]):
            out += num * 10**((len(nums)-2) - idx)

        if nums[0] == '-':
            out = -out
        if out > 2 ** 31 - 1 or -2 ** 31 > out:
            out = 0
        return out
'''
메모리 량 차이는 string 형태로 변환하여 쓰느냐 아니냐 차이 인거 같은데...?
'''
solver = Solution()
other_solver = other_solution()

print(other_solver.reverse(-123))